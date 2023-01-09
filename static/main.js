window.addEventListener("load", function() {
  // Hide the loader
  document.getElementById("loader").style.display = "none";

});

var scrollDownButton = document.getElementById("headerButton");

scrollDownButton.addEventListener("click", function() {
    var scrollPosition = 850; 
    window.scrollTo({
      top: scrollPosition,
      behavior: "smooth"});
});

let crest = document.getElementById('crestAll');
let div = document.getElementById('teamDetail');

crest.addEventListener("mouseenter", function() {
  div.style.display = 'block';
});

crest.addEventListener('mouseleave', function() {
  div.style.display = 'none';
});
