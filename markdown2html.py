#!/usr/bin/python3
'''A script markdown2html.py that takes an argument of 2 strings: -
First argument is the name of the Markdown file -
Second argument is the output file name, makes no change'''

import sys

#Convert Markdown to html
def start_script():
    #Take 2 strings arguments
    arg = len(sys.argv)

    if arg < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html ')
        exit(1)
    try:
        open('{}'.format(sys.argv[1]))
    except:
        sys.stderr.write('Missing  {}'.format(sys.argv[1]))
        exit(1)

if __name__=="__main__":
    start_script()
