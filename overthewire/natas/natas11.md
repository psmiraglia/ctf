# Natas11

*	user: `natas11`
*	pass: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`
*	url: `http://natas11.natas.labs.overthewire.org`
*	flag: `EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3`

## Procedure

1.	The hint *Cookies are protected with XOR encryption* is clear. We have to
	force an XOR-based encryption. From the theory, if `text ^ key = enc` then
	`enc ^ text = key`.

2.	By sniffing, we can get a cookie called `data` with the following content

		ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=

	Furthermore, by taking a look in the source code, there is the XOR-base
	encryption function

		function xor_encrypt($in) {
			$key = '<censored>';
			$text = $in;
			$outText = '';
			// Iterate through each character
			for($i=0;$i<strlen($text);$i++) {
				$outText .= $text[$i] ^ $key[$i % strlen($key)];
			}
			return $outText;
		}

3.	To get our key the simplest way is to define a new function as follow

		function xor_encrypt_2($in) {
			$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
			$text = $in;
			$outText = '';

			// Iterate through each character
			for($i=0;$i<strlen($text);$i++) {
				$outText .= $text[$i] ^ $key[$i % strlen($key)];
			}
			return $outText;
		}

	then use it in your local script

		<?php
			function xor_encrypt_2($in) {
				$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
				$text = $in;
				$outText = '';

				// Iterate through each character
				for($i=0;$i<strlen($text);$i++) {
					$outText .= $text[$i] ^ $key[$i % strlen($key)];
				}
				return $outText;
			}

			$mydata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff" );
			$mydata_json = json_encode($mydata);
			$mydata_enc = xor_encrypt_2($mydata_json);
			echo $mydata_enc;
		?>

	The result should be

		$ php myscript.php
		qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8'!nJq

	It seems to be a repetition of string `qw8J`. It should be the key...

4.	Create a new function like this

		function xor_encrypt_2($in) {
			//$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
			$key = "qw8J";
			$text = $in;
			$outText = '';

			// Iterate through each character
			for($i=0;$i<strlen($text);$i++) {
				$outText .= $text[$i] ^ $key[$i % strlen($key)];
			}
			return $outText;
		}

	and run the following script

		<?php
			function xor_encrypt_2($in) {
				//$key = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw=");
				$key = "qw8J";
				$text = $in;
				$outText = '';

				// Iterate through each character
				for($i=0;$i<strlen($text);$i++) {
					$outText .= $text[$i] ^ $key[$i % strlen($key)];
				}
				return $outText;
			}

			$mydata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff" );
			$mydata_json = json_encode($mydata);
			$mydata_enc = xor_encrypt_2($mydata_json);
			$mydata_b64 = base64_encode($mydata_enc);
			echo $mydata_b64;
		?>

	is should return

		$ php myscript.php
		ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK

5.	Well, let's try to use it as cookie

		$ curl -u natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK -b data=ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK http://natas11.natas.labs.overthewire.org
		<html>

		[cut]

		<h1>natas11</h1>
		<div id="content">
		<body style="background: #ffffff;">
		Cookies are protected with XOR encryption<br/><br/>

		The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3<br>

		[cut]

		</html>
