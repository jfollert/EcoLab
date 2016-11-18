import yaml
import os
import pdb
filename = "/etc/rc.local"
flag = 0
try:
    with open("commands.yaml", 'r') as stream:
        cmmds = yaml.load(stream)
        cmds = cmmds['cmd']
    for cmd in cmds:
        with open(filename, 'a+') as stream1:
            for line in stream1.readlines():
                if line != cmd:
                    flag = 1
                    continue
            if flag == 1:
                stream1.write(cmd)
                stream1.write('\n')
except IOError as e:
    if not os.access(filename, os.W_OK):
        print "Permission Denied"

