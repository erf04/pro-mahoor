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
