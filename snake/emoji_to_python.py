#! /usr/bin/env python


import sys
import tokenize
from replace_emoji import replace_emoji


def parse_file(f):
    lines = replace_emoji(tokenize.tokenize(f.readline))
    untokenize = tokenize.untokenize(lines)
    return untokenize


def emoji_to_python(inpath, outpath):
    with open(inpath, 'rb') as f, open(outpath, 'w', encoding='utf8') as n:
        n.write(parse_file(f).decode('utf8'))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("USAGE: python emoji_to_python.py inputfilepath outputfilepath")
    else:
        emoji_to_python(sys.argv[1], sys.argv[2])
