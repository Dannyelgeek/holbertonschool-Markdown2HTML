#!/usr/bin/python3

import sys

def start_script():
    arg = len(sys.argv)

    if arg < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html')
        exit(1)
    try:
        open('{}'.format(sys.argv[1]))
    except:
        sys.stderr.write('Missing {}'.format(sys.argv[1]))
        exit(1)

if __name__=="__main__":
    start_script()
