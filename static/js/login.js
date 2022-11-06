$(document).ready(function(){
    $('form').on('submit' , function(event){
        $.ajax({
            data: {
                email: $('#email').val(),
                password: $('#password').val(),
            },
            type: 'POST',
            url: '/Login',
        })
        .done(function(data){
            if (data.message == 'success'){
                window.location.replace('/');
            }
            else if (data.message == '* User Not Found'){
                $('#error').show();
                $('#error').show().text(data.message);
            }
            else{
                $('#error').show();
                $('#error').show().text(data.message);
            }
        });
        event.preventDefault();
    });
});