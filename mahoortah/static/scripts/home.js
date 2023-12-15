// window.addEventListener('DOMContentLoaded', event => {
//   const listHoursArray = document.body.querySelectorAll('.list-hours li');
//   listHoursArray[new Date().getDay()].classList.add(('today'));
// })
var dropdown = document.getElementById("dropdown");
function appear() {
  dropdown.style.display = "block";
}

function disappear() {
  dropdown.style.display = "none";
}



let carouselItems=$(".carousel-customize");
$.each(carouselItems, function (indexInArray, valueOfElement) {
  $(valueOfElement).hover(()=>{
    valueOfElement.classList.add("animate__animated", "animate__pulse");
    console.log(valueOfElement);
  },
  ()=>{
    // $(valueOfElement).removeClass("animate__animated", "animate__pulse");
    valueOfElement.classList.remove("animate__animated", "animate__pulse");
    console.log("removed");
    console.log(valueOfElement);
  }); 
   
});

let introText=document.getElementsByClassName("intro-text")[0];
let introImage=document.getElementsByClassName("intro-img")[0];
introText.classList.add("animate__animated","animate__bounceInLeft");
introImage.classList.add("animate__animated","animate__bounceInRight");


function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible)
      reveals[i].classList.add("active");
    else reveals[i].classList.remove("active");
  }
}

window.addEventListener("scroll", reveal);

window.addEventListener("load", reveal_first);
function reveal_first() {
  var revealFirst = document.getElementById("reveal-first");
  revealFirst.classList.add("active");
}
// To check the scroll position on page load
reveal();



