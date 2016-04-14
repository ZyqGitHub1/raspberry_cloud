function reflush2(result) {
	if (result['successful']) {
		result['===='].forEach(function(x) {
			var option = $('<option></option>');
			x.appendTo(option);
			option.appendTo($('#select-m-name'));
		})
	}
}

$('#section2-left').click(function() {
	$.ajax({
		type: "POST",
		url: "=========",
		success: function(result){
			reflush2(result);
		}
	});
})