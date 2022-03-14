#!/usr/bin/env python3

# prints the name and pid of this process, the name and pid of its parent, 
# the name and pid of its grandparent, and so on

import os
import sys

def read_proc_status(name):
    file = open('/proc/' + str(name) + '/status')
    lines = file.readlines()
    parsed = {}
    for line in lines:
        tv = line.split(':')
        tag = tv[0].strip()
        value = tv[1].strip()
        parsed[tag] = value
    return parsed

pid = os.getpid()
if (len(sys.argv) > 1):
    pid = sys.argv[1]
while pid != '0':
        tv = read_proc_status(pid)
        print("%12s %s" % (tv['Pid'], tv['Name']))
        pid = tv['PPid']

