const login = require("facebook-chat-api");

var user = "ajayfewell@gmail.com";
var psword = "";
// Need secure way to get username+password and login

login({email: user, password: psword}, (err, api) => {
	if (err) console.log(err);
	
	
	api.getThreadList(0, 20, "inbox", (err, arr) => {
		for (var index in arr) { 
			var friend = arr[index];
			var friendName = "";
			var friendID = friend.participantIDs[0];
			
			api.getUserInfo(friendID, (err, obj) => {
				friendName = obj.name;
				for(var prop in obj) {
					console.log(obj[prop].name);
				}
				
			});
 		}
	});
});
