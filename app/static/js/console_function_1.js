function processReflushResult(result){
	if (result['successful']) 
	{
		var electricalList = result['data']['electricalList'];
		for(var e in electricalList){
			var tr = $('#header').clone();
			tr.find(".m-name > input").val(e['electrical_name']);
			tr.find(".m-interface > input").val(e['pin']);
			tr.find(".remark > input").val(e['remark']);
			tr.find(".status > input").val(e['status']);
			tr.find(".add-or-remove > button").removeClass("btn-success").removeClass("add").addClass("btn-danger").addClass("remove").html("删除");
			tr.insertAfter($('#header'));
		}
	}else{
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
		default:
			break;
	}
}

function doAdd(name,interface,remark,status){
	var postData = {
		'electrical_name': name,
		'i': interface,
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