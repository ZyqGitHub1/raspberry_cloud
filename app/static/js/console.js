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

//switch
$(function(argument) {
    $('[type="checkbox"]').bootstrapSwitch();
})

//datetimepicker
$('.form_datetime').datetimepicker({
    //language:  'fr',
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    forceParse: 0,
    showMeridian: 1
});

// change username modal
function processChangeUsernameResult (result) {
    if ( result['successful'] ){
        window.location.href = result['url']
    } else{
        $(".change-username-body").shake(4, 15, 600);
        switch(result['error'])
        {
            case 1:
                $('#change-username-alert').removeClass('hide');
                $('#change-username-alert').html("该用户名已被使用");
                break;
            case 2:
                $('#change-username-alert').removeClass('hide');
                $('#change-username-alert').html("用户名不能为空");
                break;
            default:
                break;
        }
    }
}

function changeUsername(username) {
	var postData = {
		'username': username
	}

	$.ajax({
        type:"POST",
        url:"/auth/changeusername",
        data:postData,
        dataType:"JSON",
        success:function(result){
            processChangeUsernameResult(result);
        }
    });
}

$("#username-save").click(function(){
	var username = $('#change-username').val();
    changeUsername(username);
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
                $('#change-password-alert').html("旧密码输入错误");
                break;
            case 2:
                $('#change-password-alert').removeClass('hide');
                $('#change-password-alert').html("您两次输入的新密码不同");
                break;
            case 3:
                $('#change-password-alert').removeClass('hide');
                $('#change-password-alert').html("密码不能为空");
                break;
            default:
                break;
        }
    }
}

function changePassword(oldpassword, password, repassword){
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

// change email modal
function processChangeEmailResult (result) {
    if ( result['successful'] ){
        $('#change-email-alert2').removeClass('hide');
        $('#change-email-alert2').html(result['msg']);
    } else{
        $(".change-email-body").shake(4, 15, 600);
        $('#change-email-alert1').removeClass('hide');
        $('#change-email-alert1').html(result['msg']);
    }
}

function changeEmail(oldpassword, email) {
	var postData = {
		'oldpassword': oldpassword,
		'email': email
	}

	$.ajax({
        type:"POST",
        url:"/auth/changeemail",
        data:postData,
        dataType:"JSON",
        success:function(result){
            processChangeEmailResult(result);
        }
    });
}

$("#email-save").click(function(){
    var oldpassword = $('#change-email-oldpassword').val();
	var email = $('#change-email').val();
    changeEmail(oldpassword, email);
})

$("#logoutyes").click(function(){
    window.location.href = '/auth/logout'
})