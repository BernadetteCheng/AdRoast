$(document).ready(function() {
  $('#img_upload_button').click(function(){
    console.log("click");
    jQuery.noConflict();
    formdata = new FormData();
    var file = $('#img_upload')[0].files[0];
    if (formdata) {
        formdata.append("image", file);
        $.ajax({
          type: "POST",
          url: "http://104.248.237.28:1313/analysisPOST",
          data: formdata,
          processData: false,
          contentType: false,
          success: function(res){
            console.log('haha');
          },
          error: function(e){
            console.log('oof');
          }
        })
      }
  });
});
