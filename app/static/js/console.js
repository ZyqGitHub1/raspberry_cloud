$('#section1-left').click(function() {
	$('#section1-right').show();
	$('#section2-right').hide();
	$('#section3-right').hide();
	$('#section4-right').hide();
	$('#section5-right').hide();
})

$('#section2-left').click(function() {
	$('#section1-right').hide();
	$('#section2-right').show();
	$('#section3-right').hide();
	$('#section4-right').hide();
	$('#section5-right').hide();
})

$('#section3-left').click(function() {
	$('#section1-right').hide();
	$('#section2-right').hide();
	$('#section3-right').show();
	$('#section4-right').hide();
	$('#section5-right').hide();
})

$('#section4-left').click(function() {
	$('#section1-right').hide();
	$('#section2-right').hide();
	$('#section3-right').hide();
	$('#section4-right').show();
	$('#section5-right').hide();
})

$('#section5-left').click(function() {
	$('#section1-right').hide();
	$('#section2-right').hide();
	$('#section3-right').hide();
	$('#section4-right').hide();
	$('#section5-right').show();
})

// change password modal
function processChangePasswordResult (result) {
    if ( result['successful'] ){
        window.location.href = result['url']
    } else{
        $(".change-password-body").shake(4, 15, 600);
        switch(result['error'])
        {
            case 1:
                $('#change-password-alert').removeClass('hide');
                $('#change-password-alert').html("您两次输入的新密码不同");
                break;
            case 2:
                $('#change-password-alert').removeClass('hide');
                $('#change-password-alert').html("旧密码输入错误");
                break;
            default:
                break;
        }
    }
}

function changePassword(oldpassword, password, repassword) {
	var postData = {
		'oldpassword': oldpassword,
		'password': password,
		'repassword': repassword
	}

	$.ajax({
        type:"POST",
        url:"/auth/changepassword",
        data:postData,
        dataType:"JSON",
        success:function(result){
            processChangePasswordResult(result);
        }
    });
}

$("#password-save").click(function(){
    var oldpassword = $('#change-oldpassword').val();
	var password = $('#change-password').val();
	var repassword = $('#change-repassword').val();
    changePassword(oldpassword, password, repassword);
})