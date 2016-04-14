//show the name of machine
function reflush2(result) {
	if (result['successful']) {	
		var electricalList = result['data']['electricalList'];
		electricalList.forEach(function(x) {
			var option = $('<option></option>');
			option.html(x['electrical_name']);
			option.appendTo($('#select-m-name'));
		})
	}
}

$('#section2-left').click(function() {
	$.ajax({
		type: "POST",
		url: "/control/query_electrical",
		success: function(result){
			$('#select-m-name').empty();
			reflush2(result);
		}
	});
})

//datetimepicker
$('.addTime').click(function(){
	var datetime = $('.datetime').getTime();
	var date = new Date().parse(datetime).getTime();
	alert(datetime);
	postData = {
		'date': date
	}
	$.ajax({
		type: "POST",
		url: "====================================",
		data: postData,
		dataType: "JSON",
		success: function(result){
			//call back
		}
	})
})