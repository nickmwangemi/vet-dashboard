// Dynamic Year Change on Footer
const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

// Hide messages after 6 seconds
setTimeout(function () {
    $("#message").fadeOut("slow");
}, 2000);
  