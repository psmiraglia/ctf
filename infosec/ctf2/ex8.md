# File inclusion

1.	The normal image's upload process seems to suggest nothing special. Let's
	try to click on the `Chess 1` button. Mmmm... the linked URL is

		http://ctf.infosecinstitute.com/ctf2/exercises/ex8.php?attachment_id=1

	After some attempts on the `attachment_id` parameter, seems that for values
	from 1 to 3, the relative image is visible. For other values (e.g. 20),
	we receive the message

		This attachment is currently under review by our editors.

2.	Go back to `Chess 1` link and get the image's info. The only interesting one
	is the location where the images are stored

		http://ctf.infosecinstitute.com/ctf2/ex8_assets/img/chess1.png

3.	Since only `chess[1-3].png` are loadable (the others are "under revision"),
	we can try to overwrite one of them. Unfortunately, we can't do it...

		Try using another name for your file.

4.

[Go to Ex7](./ex7.md) | [Go to Ex9](./ex9.md)

