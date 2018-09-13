
$('[data-toggle="tooltip"]').tooltip();


$('body').on('mouseover','.art-author a', function(e){
    if(e.type == 'mouseover'){
        $(this).tooltip();
    }
});


$('.wrap-cont a').hover(function () {
    $(this).addClass('hover');
}, function () {
    $(this).removeClass('hover');
});


function mainAjax(url,data){
    $.ajax({
        url: url,
        type: 'post',
        dataType: 'json',
        data: data,
        success: function(data){
            return data;
        },
        error: function(data){
            return data;
        }
    });
}

$('a.pl-callback').click(function(){
    $(this).parent().siblings('.callback-txt').show();
});

$('a.qx').click(function(){
    $(this).parent().hide();
});