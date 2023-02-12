// Variables
let navHonkText = document.getElementById("nav-honk-text");
let navTitle = document.getElementById("nav-title");
let secretRainbow = [ "red", "orange", "yellow", "green", "cyan", "blue", "purple" ];
let secretJingles = [
    [ 0, 250, 375, 500, 750, 1250, 1500 ],
    [ 0, 500, 750, 1000, 1500, 1750, 2000, 2250, 2500, 2750, 3000 ],
    [ 0, 250, 375, 500, 750, 1000, 1250, 1375, 1500, 1750, 2000, 2250, 2375, 2500, 2750, 3000, 3500 ],
    [ 0, 166, 333, 666, 1000, 1166, 1333, 1666, 2000, 2166, 2333, 2666, 3000, 3333 ]
];
let secretKeyHistory = [];

// Events
addEventListener("keydown", event => {
    secretKeyHistory.push(event.key);
    if(secretKeyHistory.join("").endsWith("honkers")) {
        let jingle = secretJingles[Math.floor(Math.random() * secretJingles.length)];
        for(let i = 0; i < jingle.length; i++) setTimeout(() => {
            new Audio("/~/sounds/honk.mp3").play();
            navHonkText.style.color = secretRainbow[Math.floor(Math.random() * secretRainbow.length)];
            if(i >= jingle.length - 1) setTimeout(() => navHonkText.style.color = "", 500);
        }, jingle[i]);
    }
    else if(secretKeyHistory.join("").endsWith("norainbow")) {
        let elements = document.getElementsByTagName("*");
        for(let i = 0; i < elements.length; i++) elements[i].style.color = "";
        for(let i = 0; i < 5; i++) setTimeout(() => new Audio("/~/sounds/honk.mp3").play(), i * 100)
    }
    else if(secretKeyHistory.join("").endsWith("rainbow")) {
        let elements = document.getElementsByTagName("*");
        for(let i = 0; i < elements.length; i++) elements[i].style.color = secretRainbow[Math.floor(Math.random() * secretRainbow.length)];
        for(let i = 0; i < 3; i++) setTimeout(() => new Audio("/~/sounds/honk.mp3").play(), i * 100)
    }
    secretKeyHistory = secretKeyHistory.slice(-100);
});

navTitle.addEventListener("click", () => {
    if(Math.floor(Math.random() * 100) === 0) window.location.replace(`/yo${([][[]]+[])[+[]]}-${([][[]]+[])[+!![]+!![]+!![]]}gg${([][[]]+[])[+!![]+!![]+!![]]}${([][[]]+[])[+!![]+!![]]}-${([][[]]+[])[+[]]}p`);
});
