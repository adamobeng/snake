import tokenize
from collections import namedtuple


EmojiRep = namedtuple('EmojiReplacement', ['type', 'val'])


EMOJITODICT = {
    EmojiRep(tokenize.ERRORTOKEN, '⭐'): EmojiRep(None, '*'),
    EmojiRep(tokenize.ERRORTOKEN, '❔'): EmojiRep(None, 'if'),
    EmojiRep(tokenize.ERRORTOKEN, '⏩'): EmojiRep(None, 'pass'),
    EmojiRep(tokenize.ERRORTOKEN, '🌍'): EmojiRep(None, 'global'),
    EmojiRep(tokenize.ERRORTOKEN, '💔'): EmojiRep(None, 'break'),
    EmojiRep(tokenize.ERRORTOKEN, '👍'): EmojiRep(bool, 'True'),
    EmojiRep(tokenize.ERRORTOKEN, '👎'): EmojiRep(bool, 'False'),
    EmojiRep(tokenize.ERRORTOKEN, '🇫🇷'): EmojiRep(None, 'yield'),
    EmojiRep(tokenize.ERRORTOKEN, '🚫'): EmojiRep(None, 'None'),
    EmojiRep(tokenize.ERRORTOKEN, '🐑'): EmojiRep(None, 'lambda'),
    EmojiRep(tokenize.ERRORTOKEN, '🏫'): EmojiRep(None, 'class'),
    EmojiRep(tokenize.ERRORTOKEN, '📥'): EmojiRep(None, 'import'),
    EmojiRep(tokenize.ERRORTOKEN, '✌'): EmojiRep(None, 'try'),
    EmojiRep(tokenize.ERRORTOKEN, '🎀'): EmojiRep(None, 'not'),


    EmojiRep(tokenize.ERRORTOKEN, '🖨'): EmojiRep(None, 'print'),
}


DICTTOEMOJI = dict((item, key) for key, item in EMOJITODICT.items())