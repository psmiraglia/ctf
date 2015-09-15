# Natas3

*	user: `natas3`
*	pass: `sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14`
*	url: `http://natas3.natas.labs.overthewire.org`
*	flag: `Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`

## Procedure

1.	Get the page's source (e.g. `CTRL+U` on FF)

2.	At line 15, there is an HTML comment with a hint (*Not even Google will
	find it this time...*).

3.	How to disable page indexing? Simple! Use `Disallow` directive in
	`robots.txt` file. Let's try if it's available

		$ curl -u natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 http://natas3.natas.labs.overthewire.org/robots.txt
		User-agent: *
		Disallow: /s3cr3t/

4.	Let's try to list `/s3cr3t/` path. Yep! Another `users.txt` file

		$ curl -u natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
		natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
