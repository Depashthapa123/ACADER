// Script to open and close sidebar
function w3_open() {
    document.getElementById("mySidebar").style.width = "150px";
    document.getElementById("mySidebar").style.fontSize = "10px";
        for(i=0;i<5;i++){
        document.getElementsByTagName("img")[i].style.height = "50px";
        document.getElementsByTagName("img")[i].style.width = "50px";
        }
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
}
   
function w3_close() {
    document.getElementById("mySidebar").style.width = "300px";
    document.getElementById("mySidebar").style.fontSize = "";
        for(i=0;i<5;i++){
            document.getElementsByTagName("img")[i].style.height = "";
            document.getElementsByTagName("img")[i].style.width = "";
            }
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
    
}

function handleURL(url) {
    window.open(`/media/${url}`, '_blank')
}

// // function myFunction(x) {
//   if (x.matches) { // If media query matches
//     document.body.style.backgroundColor = "yellow";
//   } else {
//     document.body.style.backgroundColor = "pink";
//   }
// }

// var x = window.matchMedia("(max-width: 700px)")
// myFunction(x) // Call listener function at run time
// x.addListener(myFunction) // Attach listener function on state changes