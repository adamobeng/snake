from reversible_emojidict import EmojiMapper
import sys
import replace_emoji
import tokenize

REPLACEMENTS = EmojiMapper()

def replace_keywords(token_list):

    one = True
    for t in token_list:
        if one:
            one = False
            next

        if (t.string) in REPLACEMENTS:
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
    #Replaces python keywords in tokenized python
    #returns tokens with emojis placed
    token_list = replace_keywords(token_list)
    token_list = list(token_list)

    for token in token_list:
            print(token)
    return token_list


