$("#username").change(function() {
    var username = $(this).val();
    console.log(username)
    $.ajax({
        url : '/vendor/username_exists/',
        data : {'username' : username},
        success : function(data) {

            $("#username-error").remove();

            if (data.exists) {
                var errorMessage = $('<div id = "username-error" style = "color: red;"> This username is already taken. Please choose a different one. </div>');
                errorMessage.insertAfter("#username");
            }
        }
    });
});


$("#email").change(function() {
    var email = $(this).val();
    console.log(email)
    $.ajax({
        url : '/vendor/email_exists/',
        data : {'email' : email},
        success : function(data) {

            $("#email-error").remove();

            if (data.exists) {
                var errorMessage = $('<div id = "email-error" style = "color: red;"> This email is already taken. Please choose a different one. </div>');
                errorMessage.insertAfter("#email");
            }
        }
    });
});