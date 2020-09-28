$(document).ready(function() {
$("#upload").on('click', function() {
       $(".file-upload").click();
    });
    });

    
// Display file upload data

inputtypefile = document.getElementById('inputtypefile')
showfileslist = document.getElementById('showfileslist')

inputtypefile.addEventListener('change',function(){
    if (this.files.length > 0){
      for (var i =0; i < this.files.length; i++){
        showfileslist.innerHTML += "<p>" + this.files.item(i).name + "<span class='closeit'>X</span></p>"
      }
    }
    closeit = document.getElementsByClassName('closeit')

    arrayformclosebtn = [...closeit];
    arrayformclosebtn.forEach((onebyone) => {
      onebyone.addEventListener('click',function(e) {
        e.target.parentElement.remove()
      })
    })
})