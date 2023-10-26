"""

    Run as follows:

    10_argparse3.py (--start | --stop)

"""
import argparse
import pprint

parser = argparse.ArgumentParser(description='Personal characteristics')
parser.add_argument('-v', '--value', nargs='*', required=True)
mutual_group = parser.add_mutually_exclusive_group()
mutual_group.add_argument('--start', action='store_true')
mutual_group.add_argument('--stop', action='store_true')
args = parser.parse_args()
print(args)
