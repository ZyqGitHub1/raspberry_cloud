//show table element when onload
$(function(){
	$.ajax({
		type:"POST",
		url:"/control/query_electrical",
		success:function(result){
			processReflushResult(result);
		}
	});
})

//reflush table element
function processReflushResult(result){
	if (result['successful']) 
	{
		var electricalList = result['data']['electricalList'];
		console.log(electricalList);
		electricalList.forEach(function(x) {
			var tr = $("<tr></tr>");
			var td = new Array(5);
			for(var i = 0;i < 5;i++){
				td[i] = $("<td></td>");
			}
			for(var i = 0;i < 5;i++){
				tr.append(td[i]);
			}
			var name = $("<input type='text' class='form-control'>");
			var pin = $("<input type='text 'class='form-control' readonly='true'>");
			var remark = $("<input type='text' class='form-control'>");
			var status = $("<input id='create-switch' checked='checked' type='checkbox'>");
			var remove = $("<button class='btn btn-danger remove'>删除</button>");
			name.val(x['electrical_name']);
			pin.val(x['pin']);
			remark.val(x['remark']);			
			td[0].append(name);
			td[1].append(pin);
			td[2].append(remark);
			td[3].append(status);
			td[4].append(remove);
			tr.insertAfter($('.header'));
			$('#create-switch').bootstrapSwitch();
		});
	}
	else
	{
		alert("adsadsadasd");
	}
}

function reflush() {
	$.ajax({
		type:"POST",
		url:"/control/query_electrical",
		success:function(result){
			processReflushResult(result);
		}
	});
}

//add table element
function processAddResult(result){
	if(result['successful'])
	{
		reflush();
	}
	switch(result['error'])
	{
		case 0:
			alert("电器名不能为空");
			break;
		case 1:
			alert("电器名重复");
			break;
		case 2:
			alert("电器接口已用完");
			break;
		default:
			break;
	}
}

function doAdd(name,interface,remark,status){
	var postData = {
		'electrical_name': name,
		'pin_id': interface,
		'remark': remark,
		'status': status
	}

	$.ajax({
		type:"POST",
		url:"/control/add_electrical",
		data: postData,
		dataType: "JSON",
		success:function(result){
			processAddResult(result);
		}
	});
	
}

$('.add').click(function(){
	var name = $('.m-name > input').val();
	var interface = $('.m-interface > input').val();
	var remark = $('.remark > input').val();
	var status = $('.status > input').is(':checked');
	doAdd(name,interface,remark,status);
})

//delete table element
// $('.remove').click(function(){
// 	var name = this.parent().siblings('.m-name').val();
// 	alert(name);
// })