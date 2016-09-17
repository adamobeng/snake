#! /usr/bin/env python
"""
Functions to convert code from emojicode to python

USAGE:
emoji_to_python(inputfile) - Returns string python code
write_emoji_to_python(inputfile, outputfile) -

"""

import sys
import tokenize
from snake.replace_emoji import replace_emoji


def parse_file(f):
    lines = replace_emoji(tokenize.tokenize(f.readline))
    untokenize = tokenize.untokenize(lines)
    return untokenize


def emoji_to_python(inpath):
    """
    Open an 'emojicode' file and convert it to python

    :param inpath: File to convert to python code
    :returns: UTF-8 string python code
    """
    with open(inpath, 'rb') as f:
        return parse_file(f).decode('utf8')


def write_emoji_to_python(inpath, outpath):
    """
    Open an 'emojicode' file and convert it to python - write to a file
    :param inpath: file to convert
    :param outpath: output file
    """
    with open(outpath, 'w', encoding='utf8') as outfile:
        outfile.write(emoji_to_python(inpath))


if __name__ == '__main__':
    """
    -i to intepret the code
    outputfilepath to output to file
    """
    args = sys.argv
    if len(args) != 3:
        sys.exit("USAGE: python emoji_to_python.py [-i] inputfilepath [outputfilepath]")
    elif '-i' in args:
        args.remove('-i')
        eval(emoji_to_python(args[1]))
    else:
        write_emoji_to_python(*args)
