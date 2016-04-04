function processRegisterResult (result) {
    if ( result['isSuccessful'] == false){
         $(".form-signin > input").shake(4, 15, 600);
    }
}

function doLogin(username, password, rememberMe) {
	var postData = {
		'username': username,
		'password': password,
		'rememberMe': rememberMe
	}

	$.ajax({
        type:"POST",
        url:"/auth/login",
        data:postData,
        dataType:"JSON",
        success:function(result){
            processRegisterResult(result);
        }
    });
}

$(".btn-sign-in").click(function(){
    var username = $("#inputUsername").val();
    var password = $("#inputPassword").val();
    var rememberMe = $("#inputRememberme").is(':checked');
    doLogin(username, password, rememberMe);
})