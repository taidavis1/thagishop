function hideNav() {
	$(".navbar").removeClass("is-visible").addClass("is-hidden")
}
function showNav() {
	$(".navbar").removeClass("is-hidden").addClass("is-visible").addClass("scrolling");
}
$(document).ready(function () {
    
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
	
});