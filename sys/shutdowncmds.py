import yaml
import os
import subprocess

try:
    with open("data/shutcommands.yaml", 'r') as stream:
        cmmds = yaml.load(stream)
        script_name = cmmds['scriptname']
        file_path = cmmds['filepath']
        if not file_path.endswith('/'):
            file_path = cmmds['filepath'] + '/'
        script_path = file_path + script_name
        for cmd in cmmds['cmd']:
            with open(script_path, 'a+') as stream1:
                cmd = cmd + '\n'
                if cmd not in stream1.readlines():
                    stream1.write(cmd)
        subprocess.call('chmod a+x ' + script_path, shell=True)
        for link_path in cmmds['linkpath']:
            soft_link = 'ln -s ' + script_path + ' ' + link_path + 'K99' + script_name
            subprocess.call(soft_link, shell=True)
except IOError as e:
    if not os.access(script_path, os.W_OK):
        print "Permission Denied"
