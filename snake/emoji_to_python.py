#! /usr/bin/env python


import tokenize
from replace_emoji import replace_emoji
from sys import argv

def parse_file (f):
    lines = list()
    lines = replace_emoji(tokenize.tokenize(f.readline))
    untokenize = tokenize.untokenize(lines)

    return untokenize

try:
    f = open(argv[1], 'rb')
except IndexError:
    print ("Please enter a file to run")
    exit()


parsed = parse_file(f).decode()

n = open("unconverted.py", 'w')
n.write(parsed)

n.close()
f.close()
