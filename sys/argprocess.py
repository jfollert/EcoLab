import argparse
import sys

class ArgsProcessClient:
    def __init__(self, namef):
        self.__namef = namef
        parser = argparse.ArgumentParser(usage = self.__namef + """ <command> [<args>]
        
Commands:
    check       Returns the status of all machines.
    add         Adds a machine to the service.
    remove      Removes a machine from the service.
    wake        Turns on a machine.
    down        Turns off a machine.
    sethour     Sets a time at which a machine is turned on/off.
    """)
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print """
[ERROR] UNRECOGNIZED COMMAND ("""+ sys.argv[1]+""")!
            """
            print "use: " + __file__ + " -h\n"
            exit(1)

        getattr(self, args.command)()

    def check(self):
        parser = argparse.ArgumentParser(description='Returns the status of all machines.', usage = self.__namef + " check [-a] [-i IP/MAC]")
        parser.add_argument('-a', action='store_true', help= "Returns a list of all machines registered and their status.")
        parser.add_argument('-i', help="Returns the status (ON/OFF) of a specific machine.")
        args = parser.parse_args(sys.argv[2:])
        if args.a:
            print "Checking all machines..."
        if args.i:
            print "Checking a machine " + args.i + "..."
            print "Sending Magic Packet..."


    def add(self):
        parser = argparse.ArgumentParser(description='Adds a machine to the service.', usage = self.__namef + " add [IP:MAC]")
        parser.add_argument('ip_mac')
        args = parser.parse_args(sys.argv[2:])
        print "Adding the machine " + args.ip_mac

    def remove(self):
        parser = argparse.ArgumentParser(description='Removes a machine to the service.', usage = self.__namef + " remove [IP:MAC]")
        parser.add_argument('ip_mac')
        args = parser.parse_args(sys.argv[2:])
        print "Removing the machine " + args.ip_mac

    def wake(self):
        parser = argparse.ArgumentParser(description='Turn on a machine.', usage = self.__namef + " wake [-a] [-i]")
        parser.add_argument('-a', action='store_true', help= "Turn on all the machines registered.")
        parser.add_argument('-i', help="Turn on a specific machine.")
        args = parser.parse_args(sys.argv[2:])
        if args.a:
            print "Awaking all machines..."
        if args.i:
            print "Awaking a machine " + args.i + "..."

    def down(self):
        parser = argparse.ArgumentParser(description='Turn off a machine.', usage = self.__namef + " down [-a] [-i]")
        parser.add_argument('-a', action='store_true', help= "Turn off all the machines registered.")
        parser.add_argument('-i', help="Turn off a specific machine.")
        args = parser.parse_args(sys.argv[2:])
        if args.a:
            print "Turning off all machines..."

        if args.i:
            print "Turning off a machine " + args.i + "..."

    def sethour(self):
        parser = argparse.ArgumentParser(description='Sets the power on/off time.', usage = self.__namef + " sethour [-w] [-d]")
        parser.add_argument('-w', help= "Sets the power on time.")
        parser.add_argument('-d', help="Sets the power off time.")
        args = parser.parse_args(sys.argv[2:])
        if args.w:
            print "Setting power on time to: " + args.w
        if args.d:
            print "Setting power off time to: " + args.d
