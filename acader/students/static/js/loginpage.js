// Script to open and close sidebar
function w3_open() {
  document.getElementById("side_bar").style.display = "block";
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
   }
   
  function w3_close() {
    // var x = window.matchMedia("(style.max-width:992px)")
    // if ((document.getElementById("side_bar").style.display = "block") = x){
      document.getElementById("mySidebar").style.display = "none";
      document.getElementById("myOverlay").style.display = "none";
      document.getElementById("side_bar").style.display = "none";
    
  }
  
  // Modal Image Gallery
  function onClick(element) {
    document.getElementById("img01").src = element.src;
    document.getElementById("modal01").style.display = "block";
    var captionText = document.getElementById("caption");
    captionText.innerHTML = element.alt;
  }

