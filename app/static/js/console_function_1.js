function processAddResult(result){
	var tr = $('#header').clone();
	tr.find(".m-name > input").val(result['name']);
	tr.find(".m-interface > input").val(result['interface']);
	tr.find(".remark > input").val(result['remark']);
	tr.find(".status > input").val(result['status']);
	tr.find(".add-or-remove > button").removeClass("btn-success").removeClass("add").addClass("btn-danger").addClass("remove").html("删除");
	tr.insertAfter($('#header'));
}

function doAdd(name,interface,remark,status){
	var postData = {
		'name': name,
		'interface': interface,
		'remark': remark,
		'status': status
	}

	$.ajax({
		type:"POST",
		url:"control/add_electrical",
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