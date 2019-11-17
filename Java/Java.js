
var speed = {
	'trigger': '#speed-compare',
	'target':'.modal_content .speedometer'
};
$(window).scroll(function(){
    if ( $(this).scrollTop() > el.offset().top - 200 ) {
        el.addClass('play');
    }
    })
$(function() {
	$(speed.trigger).on('click', function() {
		setTimeout( function() { 
			$(speed.target).each(function() {
				$(this).addClass('play');
			})
		}, 1000);
	})
})