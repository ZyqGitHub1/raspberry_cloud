function processLoginResult (result) {
    if ( result['successful'] ){
         window.location.href = result['url']
    } else{
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
            processLoginResult(result);
        }
    });
}

$(".btn-sign-in").click(function login(e){
    var username = $("#inputUsername").val();
    var password = $("#inputPassword").val();
    var rememberMe = $("#inputRememberme").is(':checked');
    doLogin(username, password, rememberMe);
})

$(".form-signin > input").bind("keydown",function(e){
    if(e.keycode == 13)
        login(e);
})