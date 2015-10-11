var g_host = "www.jiajiao1.com:8088";

function log(msg){
	console.log(msg);
}

function show_msg(msg){
	$(".warn_modal").text(msg);
	$(".warn_modal").show();
	setTimeout(function(){
		$(".warn_modal").fadeOut();
	}, 3000);
}