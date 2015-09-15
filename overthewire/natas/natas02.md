# Natas2

*	user: `natas2`
*	pass: `ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi`
*	url: `http://natas2.natas.labs.overthewire.org`
*	flag: `sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14`

## Procedure

1.	Get the page's source (e.g. `CTRL+U` on FF)

2.	Statement *There is nothing on this page* is false! What about `<img>` tag?

		<img src="files/pixel.png">

3.	The image seems to be a one pixel image without any relevat info. Let's try
	if the URL `http://natas2.natas.labs.overthewire.or/files` give us
	something...

4.	BINGO! The `/files` path is listable and we can see an interesting file
	named `users.txt`. Let's try to get its conent...

		$ curl -u natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi http://natas2.natas.labs.overthewire.org/files/users.txt
		# username:password
		alice:BYNdCesZqW
		bob:jw2ueICLvT
		charlie:G5vCxkVV3m
		natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
		eve:zo4mJWyNj2
		mallory:9urtcpzBmH
