const formTitle = document.getElementById('login-title')
const userType = document.getElementById('user-type')
userType.value = 3

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

function selectAdmin(){
    formTitle.innerHTML = 'Admin Login'
    document.getElementById("admin").className = "active";
    document.getElementById("teacher").className = "";
    document.getElementById("student").className = "";
    document.getElementById("nav_admin").className = "active_navbar";
    document.getElementById("nav_student").className = "w3-bar-item w3-button w3-hover-white";
    document.getElementById("nav_teacher").className = "w3-bar-item w3-button w3-hover-white";
    userType.value = 1
    w3_close()
}

function selectTeacherLogin() {
    formTitle.innerHTML = 'Teacher Login'
    document.getElementById("teacher").className = "active";
    document.getElementById("admin").className = "";
    document.getElementById("student").className = "";
    document.getElementById("nav_teacher").className = "active_navbar";
    document.getElementById("nav_admin").className = "w3-bar-item w3-button w3-hover-white";
    document.getElementById("nav_student").className = "w3-bar-item w3-button w3-hover-white";
    userType.value = 2
    w3_close()
}
