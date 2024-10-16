import argparse
from sub import add_subparser

parser = argparse.ArgumentParser("main.py")
parser.add_argument("--org")
act = parser.add_subparsers()

add_subparser(act)

parser.parse_args()
