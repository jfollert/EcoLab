def create_argparser():
    parser = argparse.ArgumentParser(description='EcoLab')
    sp = parser.add_subparsers(dest='command')

    check_parser = sp.add_parser('check')
    check_parser.add_argument('-a', action='store_true', default=False,
            dest='all_switch',
            help='Return a list of the machines registered with their status.')
    check_parser.add_argument('-i', action='store',
            help='Return the status (ON/OFF) of a specific machine.')

    add_parser = sp.add_parser('add',
            help='Adds a machine to the service.')
    add_parser.add_argument('machine', action='store',
            help='IP:MAC')

    remove_parser = sp.add_parser('remove',
            help='Removes a machine from the service.')
    remove_parser.add_argument('machine', action='store',
            help='IP:MAC')

    wake_parser = sp.add_parser('wake')
    wake_parser.add_argument('-a', action='store_true', dest='all_swith',
            help='Turn on all the machines registered.')
    wake_parser.add_argument('-i', action='store',
            help='Turn on a specific machine.')

    down_parser = sp.add_parser('down')
    down_parser.add_argument('-a', action='store_true', dest='all_swith',
            help='Turn off all the machines registered.')
    down_parser.add_argument('-i', action='store',
            help='Turn off a specific machine.')

    return parser
