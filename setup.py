import subprocess

iptables = open("/etc/sysconfig/iptables", "r")
config = False
for linea in iptables:
    if "EcoLab" in linea:
        config = True
iptables.close()
if not config:
    iptables = open("/etc/sysconfig/iptables", "a")
    iptables.write("""
# EcoLabit
-A INPUT -p tcp --dport 5678 -j ACCEPT
""")
iptables.close()

subprocess.call(["service", "iptables", "restart"])
