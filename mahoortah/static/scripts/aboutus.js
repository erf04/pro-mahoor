function reveal() {
  var reveals = document.querySelectorAll(".animate_animated");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
        console.log("active");
    }

    else {
        reveals[i].classList.remove("active");
        console.log("remove");
    }
  }
}

window.addEventListener("scroll", reveal);

// To check the scroll position on page load
reveal();
