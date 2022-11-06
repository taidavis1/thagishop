$(document).ready(function() {

    const form_Active = document.querySelector('.active');
    const return_home = document.querySelector('#home');
    const btnNextf1 = document.querySelector('#btn-next-1')
    const btnNextf2 = document.querySelector('#btn-next-2');
    const btnPrevf2 = document.querySelector('#btn-prev-1');
    const btnPrevf3 = document.querySelector('#btn-prev-2');


    $(return_home).click(function(){

        window.location.replace('/');

    });


    $(btnNextf1).click(function(){

        let theemail = $('#email').val();

        let theemail_check = $('#re-email').val();

        $.get('/Email_Check' , {email:theemail , email_check:theemail_check} , function(response){
            if (response == "Invalid Email"){
                $('#email-error').show().text('*' + response);
            }
            else if (response == "Email Already Registered"){
                $('#email-error').show().text('*' + response);
            }
            else if(response == "Please Fill All The Fields"){
                $('#email-error').show().text('*' + response);
            }
            else if (response == "Email Does Not Match"){
                $('#email-error').show().text('*' + response);
            }
            else{
                $('#email-error').hide();
                form_Active.style.marginLeft = '-25%';
            }
        })
    });

    
    $(btnNextf2).click(function(){
        
        form_Active.style.marginLeft = '-50%';

    });

    $(btnPrevf3).click(function(){

        form_Active.style.marginLeft = '-25%';


    });

    btnPrevf2.addEventListener('click', function() {
        form_Active.style.marginLeft = '0%';
    });
    


    $('form').on('submit' , function(event){

        $.ajax({

            data: {

                email: $('#email').val(),

                agreement: $('#agreement').val(),

                first: $('#first').val(),

                last: $('#last').val(),

                phone: $('#phone').val(),

                address: $('#address').val(),

                password: $('#password').val(),

                password_check: $('#password_check').val(),


            },

            type: 'POST',

            url: '/Register',
            
        })

        .done(function(data){

            if (data.message == 'You Had Registed'){

                window.location.replace('/');
            }

            if (data.message == 'Please Fill Out All The Missing Fields'){

                $('#pass-error').show().text(data.message);

            }

            if (data.message == 'Password Does Not Match'){

                $('#pass-error').show().text(data.message);

            }


        });

        event.preventDefault();

    });



});