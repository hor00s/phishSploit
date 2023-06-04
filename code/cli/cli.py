import os
import sys
import argparse
from actions.constants import config, warning


MAX_PORT = 10_000
def port(number):
    if not 0 < number <= MAX_PORT:
        print(warning(f"Port number must be between '1 - {MAX_PORT}'. Not {number}"))
        sys.exit(1)
    config['port'] = number

def reset_config():
    os.remove(config.file_path)
    config.restore()
    config.init()

def cli():
    parser = argparse.ArgumentParser(description='My CLI')

    subparsers = parser.add_subparsers(dest='command')

    parser_port = subparsers.add_parser('port', help='Change the port that the app will be hosted on')
    parser_port.add_argument('-n', '--number', type=int, help=f"Choose a port number between '1 - {MAX_PORT}'. Current port in use: '{config['port']}'")

    parser_reset_config = subparsers.add_parser('reset_config', help="Restore app's default configuration")


    args = parser.parse_args()

    if args.command == 'port':
        if args.number is not None:
            port(args.number)
    elif args.command == 'reset_config':
        reset_config()
