var scrollDownButton = document.getElementById("headerButton");

scrollDownButton.addEventListener("click", function() {
    var scrollPosition = 850; 
    window.scrollTo({
      top: scrollPosition,
      behavior: "smooth"});
});