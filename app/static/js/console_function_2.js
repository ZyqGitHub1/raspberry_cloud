//show table element when onload
$(function(){
	$.ajax({
		type:"POST",
		url:"/control/query_clock",
		success:function(result){
			processReflush2Result(result);
		}
	});
})

//show the name of machine
function select_show(result) {
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
			select_show(result);
		}
	});
})

//datetimepicker
function processReflush2Result(result){
	if (result['successful']) 
	{
		var electricalList = result['data']['clockList'];
		electricalList.forEach(function(x) {
			var tr = $("<tr></tr>");
			var td = new Array(6);
			for(var i = 0;i < 6;i++){
				td[i] = $("<td></td>");
			}
			for(var i = 0;i < 6;i++){
				tr.append(td[i]);
			}
			var name = $("<input type='text' class='form-control' readonly='true'>");
			var pin = $("<input type='text 'class='form-control' readonly='true'>");
			var remark = $("<input type='text' class='form-control' readonly='true'>");
			var status = $("<button class='btn'></button>");
			console.log(x['status']);
			if (x['status']){
				status.addClass('btn-success').html("开");
			}else{
				status.addClass('btn-danger').html("关");
			}
			var datetime = $("<input type='text 'class='form-control' readonly='true'>");
			var remove = $("<button class='btn btn-danger remove'>删除</button>");
			remove.on('click',function(){
				var name = $(this).parent().parent().eq(0).find("input").val();
				var time = x['time']
				postData = {
					'electrical_name': name,
					'clock_time': time
				}
			
				$.ajax({
					type: "POST",
					url: "/control/delete_clock",
					data: postData,
					dataType: "JSON",
					success: function(result){
						if (result['successful']) 
						{
							$('.table3').empty();
							reflush2();
						}
					}
				});
			});			
			name.val(x['electrical_name']);
			pin.val(x['pin']);
			remark.val(x['remark']);
			var date = new Date();
			date.setTime(x['time'] * 1000);
			datetime.val(date.toLocaleString());
			td[0].append(name).attr("width","15%");
			td[1].append(pin).attr("width","12%");
			td[2].append(remark);
			td[3].append(status);
			td[4].append(datetime).attr("width","33%");
			td[5].append(remove);
			tr.appendTo($('.table3'));
		});
	}
	else
	{
		alert("adsadsadasd");
	}
}

function reflush2() {
	$.ajax({
		type:"POST",
		url:"/control/query_clock",
		success:function(result){
			processReflush2Result(result);
		}
	});
}

function processAddTimeResult(result) {
	if (result['successful']) {
		$('.table3').empty();
		reflush2();
	}
}

function doAddTime(name,date,checked) {
	var postData = {
		'electrical_name':name,
		'date': date,
		'checked': checked
	}
	$.ajax({
		type: "POST",
		url: "/control/timer",
		data: postData,
		dataType: "JSON",
		success: function(result){
			processAddTimeResult(result);
		}
	})
}

$('.addTime').click(function(){
	var name = $('#select-m-name').val();
	var datetime = $('.datetime').val();
	var checked = $('.status2 input').bootstrapSwitch('state');
	var date = Date.parse(datetime);
	doAddTime(name,date,checked);
})