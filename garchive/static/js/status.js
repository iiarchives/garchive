// Variables
let statusButton = document.getElementById("home-status-button");
let statusButtonText = document.getElementById("home-status-button-text");
let statusCacheData = localStorage.getItem("statusCacheData");
let statusCacheTimestamp = localStorage.getItem("statusCacheTimestamp")
let statusLastUpdated = 0;
let statusMembers = document.getElementById("home-status-members");
let statusPing = document.getElementById("home-status-ping");
let statusRefreshRate = 300000;
let statusTimer = document.getElementById("home-status-timer");
let statusTitle = document.getElementById("home-status-title");
let statusInterval = setInterval(() => statusUpdate(), statusRefreshRate);

// Functions
function statusButtonCooldown(seconds) {
    let timeout = seconds;
    statusButton.disabled = true;
    statusButtonText.innerText = `Updated (${timeout} s)`;
    clearInterval(statusInterval);
    statusInterval = setInterval(() => {
        timeout--;
        if(timeout <= 0) {
            statusButton.disabled = false;
            statusButtonText.innerText = "Update";
            clearInterval(statusInterval);
            statusInterval = setInterval(() => statusUpdate(), statusRefreshRate);
        }
        else {
            statusButtonText.innerText = `Updated (${timeout} s)`;
        }
    }, 1000);
}

async function statusFetch() {
    let response = await (await fetch("/status")).json();
    localStorage.setItem("statusCacheData", JSON.stringify(response));
    localStorage.setItem("statusCacheTimestamp", Date.now().toString());
    return response;
}

function statusRender(response) {
    let members = response.members;
    statusTitle.innerText = `Members (${members.length} Online)`;
    statusMembers.replaceChildren();
    for(let i = 0; i < members.length; i++) {
        let member = document.createElement("li");
        let avatar = document.createElement("img");
        let username = document.createElement("p");
        avatar.src = members[i].image;
        username.innerText = members[i].name;
        statusMembers.appendChild(member);
        member.appendChild(avatar);
        member.appendChild(username);
    }
    statusPing.innerText = `Ping: ${response.ping} ms`
}

async function statusUpdate() {
    statusLastUpdated = 0;
    statusRender(await statusFetch());
}

// Events
statusButton.addEventListener("click", () => {
    statusUpdate();
    statusButtonCooldown(15);
});

// Executes
statusCacheData && Date.now() - parseInt(statusCacheTimestamp) < statusRefreshRate ? statusRender(JSON.parse(statusCacheData)) : statusUpdate();
statusButtonCooldown(15);
setInterval(() => {
    statusLastUpdated++;
    statusTimer.innerText = `Last Updated: ${statusLastUpdated} s`;
}, 1000);
