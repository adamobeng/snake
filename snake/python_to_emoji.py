import sys
import os
import replace_emoji
from tempfile import mkstemp
import tokenize
from snake.reversible_emojidict import EmojiMapper

REPLACEMENTS = EmojiMapper()


def replace_keywords(token_list):

    one = True
    for t in token_list:
        if one:
            one = False
            continue

        if t.string in REPLACEMENTS:
            yield tokenize.TokenInfo(
                type=t.type,
                string=REPLACEMENTS[t.string],
                start=t.start,
                end=t.end,
                line=t.line
            )

        else:
            yield t


def replace_text(token_list):
    # Replaces python keywords in tokenized python
    # returns tokens with emojis placed
    token_list = replace_keywords(token_list)
    token_list = list(token_list)

    for token in token_list:
            print(token)
    return token_list


def python_to_emoji(inpath, outpath, logfile=None):

    with open(inpath, 'rb') as infile, \
            open(outpath, 'w', encoding='utf8') as outfile:
        tokens = tokenize.tokenize(infile.readline)
        emojified = replace_text(tokens)

        # Write the emoji data to a log file if required
        if logfile:
            with open(logfile, 'w', encoding='utf8') as lf:
                lf.write(str(emojified))

        emojicode = tokenize.untokenize(emojified)

        if logfile:
            print(emojicode)

        outfile.write(emojicode)

if __name__ == '__main__':
    if 3 <= len(sys.argv) <= 4:
        python_to_emoji(*sys.argv[1:])
    else:
        sys.exit('USAGE: python_to_emoji inputfilepath outputfilepath (logfile)')
