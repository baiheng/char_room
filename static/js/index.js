$(document).ready(function(){
	var ws = null;
	var close = false;

	$("#id_join").on('click', function(){
		if(ws == null){
			close = false;
		    connect_ws();
		}else{
			show_msg("你已经在聊天室中");
		}
	});

	$("#id_leave").on('click', function(){
		if(ws == null){
			show_msg("没有加入聊天室");
			return;
		}else{
			close = true;
			ws.close();
			ws = null;
		}
	});

	$("#id_send").on('click', function(){
		var msg = $("#id_chat_msg").val();
		if(msg == ""){
			show_msg("发送消息不能为空");
			return;
		}
		if(ws == null){
			show_msg("没有加入聊天室不能发送消息");
			return;
		}
		ws.send(msg);
		$("#id_chat_panel").append("<p>我: " + msg + "</p>");
		$('#id_chat_panel').scrollTop( $('#id_chat_panel')[0].scrollHeight );
		$("#id_chat_msg").val("");
	});

	function connect_ws(){
		var ws_url = "ws://" + g_host + "/chat_websocket";
		ws = new WebSocket(ws_url);
		ws.onopen = function(){
			log("ws open");
		};
		ws.onmessage = function(evt){
			log("ws msg " + evt.data);
			$("#id_chat_panel").append("<p>" + evt.data + "</p>");
			$('#id_chat_panel').scrollTop( $('#id_chat_panel')[0].scrollHeight );
		};
		ws.onclose = function(evt){
			log("ws close");
			if(close == false){
				setTimeout(function(){
					connect_ws();
				}, 1000);
			};
		};
		ws.onerror = function(e) {
			log("ws error" + e);
		};
	}
});

