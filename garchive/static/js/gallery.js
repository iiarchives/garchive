// Variables
let galleryCount = 0;
let galleryElement = document.getElementById("details-gallery-images");
let galleryLimit = 0;
let galleryMax = 0;
let galleryPage = document.getElementById("details-gallery-page");

// Functions
function galleryNext() {
    if((galleryCount + 1) * galleryLimit >= galleryImages.length) return;
    galleryCount++;
    galleyRender();
}

function galleryPrevious() {
    if(galleryCount <= 0) return;
    galleryCount--;
    galleryPage.innerText = galleryCount.toString() + " of " + galleryMax.toString();
    galleyRender();
}

function galleyRender() {
    galleryElement.replaceChildren();
    galleryPage.innerText = (galleryCount + 1).toString() + " of " + galleryMax.toString();
    let images = galleryImages.slice(galleryCount * galleryLimit, (galleryCount + 1) * galleryLimit);
    if(!images.length) {
        let message = document.createElement("p");
        message.innerText = "The gallery is empty! Come back later~";
        galleryElement.appendChild(message);
        return;
    }
    for(let i = 0; i < images.length; i++) {
        let container = document.createElement("a");
        let image = document.createElement("img");
        let fileName = document.createElement("p");
        container.href = galleryStatic  + images[i].slice(0, -3) + "png";
        image.src = galleryStatic + images[i].slice(0, -3) + "webp";
        fileName.innerText = images[i];
        container.appendChild(image);
        container.appendChild(fileName);
        galleryElement.appendChild(container);
    }
}

function galleryResize() {
    let previous = galleryLimit;
    galleryLimit = window.innerWidth < 1000 ? 5 : 20;
    if(previous === galleryLimit) return;
    galleryCount = Math.round(galleryCount * previous / galleryLimit);
    galleryMax = Math.max(Math.ceil(galleryImages.length / galleryLimit), 1);
    galleyRender();
}

// Events
addEventListener("resize", () => galleryResize());

// Executes
galleryResize();
