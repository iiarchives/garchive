"use strict";
// Variables
let mainSections = document.getElementsByClassName("main-section");
// Loops
for (let i = 0; i < mainSections.length; i++) {
    let mainSection = mainSections[i];
    let image = document.createElement("img");
    image.src = "/~/svgs/link.svg";
    image.height = 20;
    mainSection.appendChild(image);
    mainSection.onclick = () => window.location.hash = mainSection.id;
}
