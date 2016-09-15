#!/usr/bin/env python3

import tokenize
from replace_emoji import replace_emoji, output_formatter
import argparse
from sys import argv

def parse_file (f):
    lines = list()
    lines = replace_emoji(tokenize.tokenize(f.readline))
    untokenize = tokenize.untokenize(lines)

    return untokenize

f = open(argv[1], 'rb')
eval(parse_file(f))

