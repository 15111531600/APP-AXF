$(function () {
    $('#username').blur(function () {
        if(!$(this).val){
            $('#nameTips').html('用户名不合法')
        }else{
            $('#nameTips').html('用户名合法')
        }
    });
    $('#password').blur(function () {
        if(!$(this).val){
            $('#psdTips').html('密码不合法')
        }
    });
    $('#repassword').blur(function () {
        if($(this).val != $('#repassword').val){
            $('#psdTips').html('两次密码不一致')
        }
    });
    $('#email').blur(function () {
        if(!$(this).val){
            $('#emailTips').html('邮箱不合法')
        }else{
            $('#psdTips').html('密码不合法')
        }
    });
    $('#files').blur(function () {
        if (!$(this).val) {
            $('#iconTips').html('不合法')
        }
    });
});