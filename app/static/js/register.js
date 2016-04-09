function processRegisterResult (result) {
    if ( result['successful'] ){
        window.location.href = result['url']
    } else{
        $(".form-register").shake(4, 15, 600);
        switch(result['error'])
        {
            case 1:
                $('#register-alert').removeClass('hide');
                $('#register-alert').html("用户名不能为空");
                break;
            case 2:
                $('#register-alert').removeClass('hide');
                $('#register-alert').html("用户名已存在");
                break;
            case 3:
                $('#register-alert').removeClass('hide');
                $('#register-alert').html("密码不能为空");
                break;
            case 4:
                $('#register-alert').removeClass('hide');
                $('#register-alert').html("两次密码不同");
                break;
            default:
                break;
        }
    }
}

function doRegister(username, email, password, repassword) {
	var postData = {
		'username': username,
        'email': email,
		'password': password,
		'repassword': repassword
	}

	$.ajax({
        type:"POST",
        url:"/auth/register",
        data:postData,
        dataType:"JSON",
        success:function(result){
            processRegisterResult(result);
        }
    });
}

$("#register-ok").click(function(){
    var username = $("#register-username").val();
    var email = $("#register-email").val();
    var password = $("#register-password").val();
    var repassword = $("register-confirm-password").val();
    doRegister(username, email, password, repassword);
})

$("#register-cancel").click(function(){
    $('#register-alert').addClass('hide');
})