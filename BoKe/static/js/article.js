

$('.pl-sub').click(function(){
	var val = $('#pl-text').val();
	$(this).parent().find('.false').fadeIn();
        setTimeout(function () {
            $('.false').fadeOut()
        }, 3500);

	if(val == ''){
		$(this).parent().find('.false span').html('');
	}
});