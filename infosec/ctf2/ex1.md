# A3 Cross-Site Scripting (XSS)

1.	Let's try to use `test` as "Site Name" and `http://www.example.com` as
	"Site URL". It works as expected.

2.	Now, change `test` in `<test>` just to check if input validation in present.
	Is it...

3.	At first, we need to disable input validation. According to the source,
	"Site Name" is validated against a RegEx (`[a-zA-Z]+`). To allow "special"
	characters, two approaches can be followed:

	*	Change the RegEx in `.+`

			<input type="text" placeholder="Name of site" maxsize="10" class="form-control" pattern=".+" required name="name"/>
			                                                                                         ^^

	*	Add the `formnovalidate` attribute to the `submit` input

			<input type="submit" class="btn btn-md btn-primary" value="Add Link" formnovalidate/>
			                                                                     ^^^^^^^^^^^^^^

	Both the approaches can be implemented by using FF's Web Developer tools.

4.	Let's try to inject the solution's code `<script>alert('Ex1');</script>` by
	using "Site Name" field. It works, but unfortunately `<` and `>` characters
	are escaped (see `../js/ex1.js:18-19`)

		var siteName = $(".ex1 input[type='text']").val().trim().replace(/</g, "&lt;").replace(/>/g, "&gt;");
		var siteURL = $(".ex1 input[type='url']").val().trim().replace(/</g, "&lt;").replace(/>/g, "&gt;");

5.	To bypass escaping, we can use the JS debugger provided by FF. Let's add a
	breackpoint at line 18. After the code execution (the string escaping) we
	can manually modify the value of "Site Name" by re-inserting the original
	value without escapes (`<script>alert('Ex1');</script>`). That's it!

[Go to Exercise2](./ex2.md)

