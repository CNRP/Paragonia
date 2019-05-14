$(document).on('click', '#click-me', () => {
    $('#info-modal').addClass("show");
})

$(document).ready(function(){
	$(".modal-dialog .close").click(function(){
		$(this).closest(".modal-dialog").removeClass("show"); 
	});
});