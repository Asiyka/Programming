function message(text){
	jQuery("#chat-result").append(text);
}
 jQuery(document).ready(function($) {

 	var socket = new WebSocket("ws://localhost:8090/chat/server.php");

 	socket.onopen = function() {
 			message("<div>Звязок є</div>")
 	};

 	socket.onerror = function(error) {
 		message("<div>Помилка" + (error.message ? error.message : "") + "</div>");
 	};

 	socket.onclose = function() {
 		message("<div>Звязок закрито</div>");
 	};

 	socket.onmessage = function(event) {
 		var data = JSON.parse(event.date);
 		message("<div> + data.type + " -"  + data.message + </div>");
 	}

 });