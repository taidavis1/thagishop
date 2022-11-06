function hideNav() {
	$(".navbar").removeClass("is-visible").addClass("is-hidden")
}
function showNav() {
	$(".navbar").removeClass("is-hidden").addClass("is-visible").addClass("scrolling");
}
$(document).ready(function () {
    
    $(".navbar").removeClass("is-visible").addClass("is-hidden");

    $('#logo-home').click(function(event){
        
        window.location.replace('/');
        
        event.preventDefault();
        
    });
    
	var Scroll1 = 0;
	$(window).scroll(function () {
		var Scroll2 = $(this).scrollTop();
		
        if (Scroll2 > 0 && Scroll2 < $(document).height() - $(window).height()) {
			if (Scroll2 > Scroll1) {
				hideNav();
			} 
            else {
				showNav();
			}
			Scroll1 = Scroll2;
		}
	});
	$('#tri-carsoul-item').carousel({
		interval: 2000
	})
	$('#Shop').click(function(event){
		$.ajax({
			url: '/check_user',
			type: 'GET',
			success: function(data){
				if (data.msg == 'done'){
					window.location.replace('/Shop');
				}
				else{
					alert('You Need To Log In First');
				}
			}
		})
        event.preventDefault();
	});
	$.ajax({
		url: '/',
		type: 'POST',
		dataType: 'json',
		success: function(data){
			if (data.user != 'none'){
				$('#login_text').text(data.user);
				$('.log-link').removeAttr('href');
				$('#log-btn').hover(function(){
					$('#login_text').text('Logout');
					}, function(){
					$('#login_text').text(data.user);
				});
				$('#log-btn').click(function(){
					window.location.replace('/Logout');
				});
			}
		}
	});
});