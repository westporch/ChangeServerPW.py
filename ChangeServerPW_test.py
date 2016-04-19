#!/usr/bin/python

import os
import sys

def file_to_dict(filename):
    result = dict()
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        item = line.split()
        server_ip = item[0]
        users = item[1].split(',')

        result[server_ip] = users
    f.close()

    return result

def pwchange(serverip, user, oldpw=None, newpw=None):
    print("%s %s %s %s" % (serverip, user, oldpw, newpw))
    os.system('sshpass -p %s ssh %s -l%s "echo \"%s:%s\" | chpasswd " ' % (oldpw, serverip, user, user, newpw))
    #os.system('echo "%s:%s" | chpasswd' % (user, newpw))
#    os.system('echo "%s:%s"' % (user, newpw))

    # os.system('passswd user')
    return 0


filename = sys.argv[1]
oldpw = sys.argv[2]
newpw = sys.argv[3]

data = file_to_dict(filename)

for server in data:
    for user in data[server]:
        pwchange(server, user, oldpw, newpw)
