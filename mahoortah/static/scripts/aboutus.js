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


