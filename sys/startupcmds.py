import yaml
import os

# import pdb
filename = "/etc/rc.local"
try:
    with open("data/startcommands.yaml", 'r') as stream:
        cmmds = yaml.load(stream)
        cmds = cmmds['cmd']
    for cmd in cmds:
        with open(filename, 'a+') as stream1:
            cmd = cmd + '\n'
            if cmd not in stream1.readlines():
                stream1.write(cmd)

except IOError as e:
    if not os.access(filename, os.W_OK):
        print "Permission Denied"
