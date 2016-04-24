$('.close-camera').click(function() {
	$('.camera').empty();
})

$('.open-camera').click(function() {
	var pic = $('<img src="control/video_feed">');
    pic.appendTo($('.camera'));
})