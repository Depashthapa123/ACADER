//document.querySelector('.image').addEventListener('mouseenter', function (event){
//    event.target.style.width = '120px'
//    event.target.style.height = '120px'
//})
//
//document.querySelector('.image').addEventListener('mouseout', function (event){
//    event.target.style.width = '60px'
//    event.target.style.height = '60px'
//})

// Script to open and close sidebar
function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
    document.getElementById("side_bar").style.display = "block";
}
   
function w3_close() {

      document.getElementById("mySidebar").style.display = "none";
      document.getElementById("myOverlay").style.display = "none";
      document.getElementById("side_bar").style.display = "none";
    
}

function handleURL(url) {
    window.open(`/media/${url}`, '_blank')
}


// function reload(){
//     setTimeout(function () {
//         if(window.location.hash != '#r') {
//             window.location.hash = 'r';
//             window.location.reload(1);
//         }
//     },2000);
// }