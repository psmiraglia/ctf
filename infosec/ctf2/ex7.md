# A3 Cross-Site Scripting (XSS)

1.	Let's take a look at the form's source code

		<form class="ex7-form" action="">
		<label for="name">    <span class="glyphicon glyphicon-user"></span>Username:</label>
		<input type="text" id="name" name="name" class="form-control input-lg"/>
		<label for="pass">   <span class="glyphicon glyphicon-lock"></span>Password:</label>
		<input type="password" id="pass" name="pass" class="form-control input-lg"/>
		<input name="action" type="hidden" value='/ctf2/exercises/ex7.php               '>
		<div>
		<input type="submit" class="btn btn-lg btn-default" value="Login"/>
		<input type="reset" class="btn btn-lg btn-danger" value="Reset"/>
		</div>
		</form>

	As we can see, there is an hidden field named `action`

		<input name="action" type="hidden" value='/ctf2/exercises/ex7.php               '>

	Seems to be interesting...

2.	If we're lucky, the hidden field's value is set by referring the
	`$_SERVER["PHP_SELF"]` variable. To check it, we could try with the
	following URL

		http://ctf.infosecinstitute.com/ctf2/exercises/ex7.php/foo

	Yep! As we can see, there are some changes in the web page's rendering.
	Furthermore, the form's source code changed in

		<form class="ex7-form" action="">

		[...]

		<input name="action" type="hidden" value='/ctf2/exercises/ex7.php/foo               '>

		[...]

		</form>

	This will be our attack's vehicle.

3.	Our goal now is to create a "magic" URL that will include the code

		<h1>YOUR NAME HERE</h1>

	in the page. Let's try by visiting the URL

		http://ctf.infosecinstitute.com/ctf2/exercises/ex7.php/'>foo

	As we can see, the string `foo '>` appeared between the password field and
	the buttons. It seems to be the right way. Let's try with

		http://ctf.infosecinstitute.com/ctf2/exercises/ex7.php/'><h1>GotTheMilk</h1>

	Yep!

[Go to Ex6](./ex6.md) | [Go to Ex8](./ex8.md)

