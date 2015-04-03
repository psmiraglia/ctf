# Natas8

*	user: `natas8`
*	pass: `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`
*	url: `http://natas8.natas.labs.overthewire.org`
*	flag: `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`

## Procedure

1.	This seems to be similar to Natas6. Let's click on `View sourcecode`

		<?

		$encodedSecret = "3d3d516343746d4d6d6c315669563362";

		function encodeSecret($secret) {
			return bin2hex(strrev(base64_encode($secret)));
		}

		if(array_key_exists("submit", $_POST)) {
			if(encodeSecret($_POST['secret']) == $encodedSecret) {
			print "Access granted. The password for natas9 is <censored>";
			} else {
			print "Wrong secret";
			}
		}
		?>

2.	Secret `3d3d516343746d4d6d6c315669563362` seems to be a HEX string.
	Decode it

		$ echo -n 3d3d516343746d4d6d6c315669563362 | perl -pe 's/([0-9a-f]{2})/chr hex $1/gie'
		==QcCtmMml1ViV3b

	It's a reversed Base64 string. Let's try to decode it

		$ echo "==QcCtmMml1ViV3b" | rev | base64 -d
		oubWYf2kBq

3.	Let's try to use `oubWYf2kBq` secret

		Access granted. The password for natas9 is
		W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
