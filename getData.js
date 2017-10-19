const login = require("facebook-chat-api");

user = "ajayfewell@gmail.com";
pword = "0";
// Need secure way to get username+password and login

login({email: user, password: pword}, (err, api) => {
	if (err) console.log(err);
	
	
})
