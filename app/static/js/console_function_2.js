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
		var electricalList = result['data']['electricalList'];/////////////////////////
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
			var remark = $("<input type='text' class='form-control'>");
			var status = $("<input class='create-switch' type='checkbox'>");
			status.on('switchChange.bootstrapSwitch', function(event, state) {
  				id = x['pin'];
				var postData = {
					'pin_id': id,
					'status': state
				}
		
				$.ajax({
					type: "POST",
					url: "/control/switch",
					data: postData,
					dataType: "JSON",
					success: function(result){
						
					}
				});
			});
			var datetime = $("<input type='text 'class='form-control' readonly='true'>");
			var remove = $("<button class='btn btn-danger remove'>删除</button>");
			remove.on('click',function(){
				var name = $(this).parent().parent().eq(0).find("input").val();
				postData = {
					'electrical_name': name
				}
			
				$.ajax({
					type: "POST",
					url: "/control/delete_electrical",
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
			status.attr("checked",x['status']);		
			datetime.val(x['datetime']);/////////////////
			td[0].append(name);
			td[1].append(pin);
			td[2].append(remark);
			td[3].append(status);
			td[4].append(datetime);
			td[5].append(remove);
			tr.appendTo($('.table3'));
			$('.create-switch').bootstrapSwitch();
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
		url:"===================================================",
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
	var checked = $('.status2 > input').attr('checked');
	var date = Date.parse(datetime);
	doAddTime(name,date,checked);
})