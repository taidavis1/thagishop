function delete_cart_item(id){

    $.ajax({

        url: '/remove-item-cart' + '/' + id,

        type: 'GET',

        success: function(data){

            window.location.reload();

        }

    })

}

function add(id , quantity){

    $.ajax({

        url: '/add-quantity' + '/' + id + '/' + quantity,

        type: 'GET',

        success: function(data){

            $('#quantity' + id).val(data.done);

            $('#total').text("Total: " + data.total);

            $('#total-payment').val(data.total);


        }

    })

}

function minus(id , quantity){

    $.ajax({

        url: '/minus-quantity' + '/' + id + '/' + quantity,

        type: 'GET',

        success: function(data){

            if (data.done){

                $('#quantity' + id).val(data.done);

                $('#total').text("Total: " + data.total);

                $('#total-payment').val(data.total);

            }

            else{

                window.location.reload();

            }
        }

    })

}


$(document).ready(function(){

    $('#shop').click(function(){

        window.location.replace('/Shop');
            
    });

});
