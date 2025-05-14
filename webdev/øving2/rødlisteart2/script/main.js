const heading = document.querySelector("#header");
heading.setHTMLUnsafe("Eksempel på rødlisteart");


let counter = 0;
const header = document.getElementById("header");
header.addEventListener("click", function() {
    counter++;
    alert(`Au! Du har trykket med ${counter} ganger!`);
});


const about_button = document.querySelector("#about");
about_button.addEventListener("click", function() {
    alert("Dette er et nettsted om rødlistede fuglearter");
});