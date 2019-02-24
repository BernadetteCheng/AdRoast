(function($) {
  $img_form = $("#img_upload"),
  $upload_button = $("#img_upload_button");

  $upload_button.onClick({
    console.log("click");
    /*
    jQuery.noConflict();
    formdata = new FormData();
    var file = $img_form.prop('files');
    if (formdata) {
        formdata.append("image", file);
        jQuery.ajax({
            url: "http://104.248.237.28:1313/analysisPOST",
            type: "POST",
            data: formdata,
            processData: false,
            contentType: false,
            success:function(res){
              console.log('haha');
            },
            failure:function(e){
              console.log('oof');
            }
        });
      }
    */
    })
})(jQuery);
