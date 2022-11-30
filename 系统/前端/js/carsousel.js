document.write("<script src='../js/jquery-3.6.0.js'></script>")
window.onload=function(){
    $.ajax({
        type: "get",
        url: "http://localhost:8080/user",
        success: function(msg){
          console.log(msg[0].name)
        }
     });
}