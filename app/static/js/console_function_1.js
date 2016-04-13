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
  			var tr = $('#header').clone();
			tr.find(".m-name > input").val(x['electrical_name']);
			tr.find(".m-interface > input").val(x['pin']);
			tr.find(".remark > input").val(x['remark']);

			var newButton = $("<input type="checkbox" checked/>");
			newButton.attr("checked",x['status']);
			var oldButton = tr.find(".status > input");
			tr.find(".status").replaceChild(newButton,oldButton);

			var removeButton = $("<button class="btn btn-danger remove">删除</button>");
			var addButton = tr.find(".add-or-remove > button");
			tr.find(".add-or-remove").replaceChild(removeButton,addButton);
			tr.insertAfter($('#header'));
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