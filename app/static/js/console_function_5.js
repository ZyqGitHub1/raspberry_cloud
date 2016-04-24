$('#m_switch_open').click(function() {
	var postData = {
		'status': true
	}

	$.ajax({
		type: "POST",
		url: "control/mail/switch",
		data: postData,
		dataType: "JSON",
		success: function(result) {
			if (result['successful']) {
				alert('发信打开');
			}
		}
	});
})

$('#m_switch_close').click(function() {
	var postData = {
		'status': false
	}

	$.ajax({
		type: "POST",
		url: "control/mail/switch",
		data: postData,
		dataType: "JSON",
		success: function(result) {
			if (result['successful']) {
				alert('发信关闭');
			}
		}
	});
})

$('#t_switch_open').click(function() {
	var postData = {
		'status': true
	}

	$.ajax({
		type: "POST",
		url: "control/temperature/switch",
		data: postData,
		dataType: "JSON",
		success: function(result) {
			if (result['successful']) {
				alert('测温打开');
			}
		}
	});
})

$('#t_switch_close').click(function() {
	var postData = {
		'status': false
	}

	$.ajax({
		type: "POST",
		url: "control/temperature/switch",
		data: postData,
		dataType: "JSON",
		success: function(result) {
			if (result['successful']) {
				alert('测温关闭');
			}
		}
	});
})
