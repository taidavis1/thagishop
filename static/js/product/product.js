$(document).ready(function(){

    $('form').on('submit' , function(event){

        $.ajax({
            data: {
                product_name: $('#product_name').val(),

                product_img: $('#product_img').val(),

                description: $('#description').val(),

                quantity: $('#quantity').val(),

                price: $('#price').val(),
            },
            type: 'POST',
            url: '/Add_Product',
            contentType: false,
            cache: false,
            processData: true,
        })
        .done(function(data){

            if (data.message == 'Add Successfull'){

                $('#message').show().text(data.message);

                $('#product_name').val('');

                $('#product_img').val(null);

                $('#description').val('');

                $('#quantity').val('');
            }
        });

        event.preventDefault();


    });


});