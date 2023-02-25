// Variables
let statusCache: statusResponse | null = null;
let statusClock = document.querySelector("#status-clock") as HTMLSpanElement;
let statusLatency = document.querySelector("#status-latency") as HTMLSpanElement;
let statusMemberCount = document.querySelector("#status-membercount") as HTMLSpanElement;
let statusMemberList = document.querySelector("#status ul") as HTMLUListElement;
let statusPopUp = document.querySelector("#status-uuid") as HTMLSpanElement;
let statusRefresh = document.querySelector("#status-update img") as HTMLImageElement;

// Functions
async function statusFetch(force: boolean = false): Promise<boolean> {
    if(statusCache === null) {
        console.log("Loading status cache...");
        let cache = localStorage.getItem("statusCache");
        if(cache !== null) {
            statusCache = JSON.parse(cache);
            console.log("Status cache found!");
            return true;
        }
        console.warn("Status cache miss! Refetching...");
    }
    if(force || statusCache === null || Date.now() - statusCache.timestamp > 300000) {
        console.log("Fetch status...");
        let response: statusResponse = await (await fetch("/api/status")).json();
        localStorage.setItem("statusCache", JSON.stringify(response));
        statusCache = response;
        console.log("Status fetched successfully!");
        return true;
    }
    return false;
}

function statusUpdate(force: boolean = false): void {
    statusFetch(force).then(statusFetched => {
        if(statusCache !== null) {
            statusClock.innerText = `Last Updated: ${Math.max(Math.round((Date.now() - statusCache.timestamp) / 1000), 0)}s Ago`;
            if(force) {
                statusRefresh.style.transform = "rotate(720deg)";
                statusRefresh.style.transition = "transform ease 1.5s";
                setTimeout(() => statusRefresh.style.transform = statusRefresh.style.transition = "", 1500);
            }
            if(statusFetched) {
                statusMemberCount.innerText = `${statusCache.members.length} Members Online`;
                (statusLatency.childNodes[0] as Text).data = `${statusCache.ping}ms `;
                statusMemberList.replaceChildren();
                for(let i = 0; i < statusCache.members.length; i++) {
                    let member = statusCache.members[i];
                    let listItem = document.createElement("li");
                    let span = document.createElement("span");
                    span.innerHTML = `<img src="https://crafatar.com/avatars/${member.id}?size=20&overlay"> ${member.name}`;
                    listItem.onclick = event => setTimeout(() => {
                        statusPopUp.innerHTML = `UUID: <em>${member.id}</em>`;
                        statusPopUp.style.transform = "scale(100%)";
                        statusPopUp.style.left = `${event.clientX - statusPopUp.clientWidth / 2}px`;
                        statusPopUp.style.top = `${event.clientY - 50}px`;
                    });
                    listItem.appendChild(span);
                    statusMemberList.appendChild(listItem);
                }
            }
        }
    });
}

// Events
statusMemberList.onscroll = () => statusPopUp.style.transform = "scale(0%)";
addEventListener("click", statusMemberList.onscroll);
addEventListener("scroll", statusMemberList.onscroll);

// Loops
setInterval(() => statusUpdate(), 250);
statusUpdate();