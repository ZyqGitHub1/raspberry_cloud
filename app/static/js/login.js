function doLogin(username, password, rememberMe) {
	var postData = {
		'username': username,
		'password': password,
		'rememberMe': rememberMe
	}

	$.post('/author/login',postData,function(data){
		if(data.successful == false)
			$(".form-signin > input").shake(4,15,600)
	})
}

$(".btn-sign-in").click(function(){
    var username = $("#inputUsername").val();
    var password = $("#inputPassword").val();
    var rememberMe = $("#inputRememberme").is(':checked');
    doLogin(username, password, rememberMe);
})