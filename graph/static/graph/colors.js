//This part below handles the color modes by setting the html page to the css type
var setMode = localStorage.getItem('theme');
console.log('theme:', setMode);

if (setMode == null) {
    defaultMode('defaultCSS');
}
else if (setMode == 'defaultCSS') {
    defaultMode('defaultCSS');
}
else if (setMode == 'darkmodeCSS') {
    darkMode('darkmodeCSS');
}
else if (setMode == 'protanopiaCSS') {
    protanopiaMode('protanopiaCSS');
}
else if (setMode == 'deuteranopiaCSS') {
    deuteranopiaMode('deuteranopiaCSS');
}
else if (setMode == 'tritanopiaCSS') {
    tritanopiaMode('tritanopiaCSS');
}
else if (setMode == 'monochromaCSS') {
    monochromaMode('monochromaCSS');
}

function defaultMode(content) {
    let elementBody = document.body;
    elementBody.className = "body";

    //let content = document.getElementById("defaultID"); //html id name
    content.innerText = "Default"; //testing
    localStorage.setItem('theme', content); //saves to local storage

    let image1 = document.getElementById("step1");
    let image2 = document.getElementById("step2");
    let image3 = document.getElementById("step3");
    image1.src = "https://i.ibb.co/SfDTf84/step1.jpg";
    image2.src = "https://i.ibb.co/4m4ddWD/step2.jpg";
    image3.src = "https://i.ibb.co/jvmLfpF/step3.jpg";
}
function darkMode(content) {
    let elementBody = document.body;
    elementBody.className = "darkmode"; //css class name
    
    //const elementBody = document.getElementById("darkmode");
    //let sheet = document.getElementById("darkmodeID");
    //let content = document.getElementById("darkmodeID"); //html id name
    //document.getElementById('darkmodeID') = sheet
    content.innerText = "Dark Mode"; //testing
    localStorage.setItem('theme', content); //saves to local storage

    let image1 = document.getElementById("step1");
    let image2 = document.getElementById("step2");
    let image3 = document.getElementById("step3");
    image1.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image2.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image3.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
}
function protanopiaMode(content) {
    let elementBody = document.body;
    elementBody.className = "protanopia";

    //let content = document.getElementById("protanopiaID"); //html id name
    content.innerText = "Protanopia"; //testing
    localStorage.setItem('theme', content); //saves to local storage

    let image1 = document.getElementById("step1");
    let image2 = document.getElementById("step2");
    let image3 = document.getElementById("step3");
    image1.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image2.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image3.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
}
function deuteranopiaMode(content) {
    let elementBody = document.body;
    elementBody.className = "deuteranopia";

    //let content = document.getElementById("deuteranopiaID"); //html id name
    content.innerText = "Deuteranopia"; //testing
    localStorage.setItem('theme', content) //saves to local storage

    let image1 = document.getElementById("step1");
    let image2 = document.getElementById("step2");
    let image3 = document.getElementById("step3");
    image1.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image2.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image3.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
}
function tritanopiaMode(content) {
    let elementBody = document.body;
    elementBody.className = "tritanopia";

    //let content = document.getElementById("tritanopiaID"); //html id name
    content.innerText = "Tritanopia"; //testing
    localStorage.setItem('theme', content) //saves to local storage

    let image1 = document.getElementById("step1");
    let image2 = document.getElementById("step2");
    let image3 = document.getElementById("step3");
    image1.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image2.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image3.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
}
function monochromaMode(content) {
    let elementBody = document.body;
    elementBody.className = "monochroma";

    //let content = document.getElementById("monochromaID"); //html id name
    content.innerText = "Monochroma"; //testing
    localStorage.setItem('theme', content) //saves to local storage

    let image1 = document.getElementById("step1");
    let image2 = document.getElementById("step2");
    let image3 = document.getElementById("step3");
    image1.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image2.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
    image3.src = "https://i.ibb.co/pZZRGV0/logo-removebg-preview.png";
}