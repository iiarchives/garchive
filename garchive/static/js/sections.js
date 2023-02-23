"use strict";
// Variables
let sections = document.getElementsByClassName("section");
// Loops
for (let i = 0; i < sections.length; i++) {
    let section = sections[i];
    let image = document.createElement("img");
    image.src = "/~/svgs/link.svg";
    image.height = 20;
    section.appendChild(image);
    section.onclick = () => window.location.hash = section.id;
}
