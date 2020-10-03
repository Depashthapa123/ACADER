window.history.pushState({page: 1}, "", "");

window.onpopstate = function(event) {
    if(event){
        window.location.href = "/student_list";
        // Code to handle back button or prevent from navigation
    }
}

