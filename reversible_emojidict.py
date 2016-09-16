import tokenize
from collections import namedtuple


EmojiRep = namedtuple('EmojiReplacement', ['type', 'val'])


REPLACEMENTS = [
    (EmojiRep(tokenize.ERRORTOKEN, '⭐'), EmojiRep(None, '*')),
    (EmojiRep(tokenize.ERRORTOKEN, '❔'), EmojiRep(None, 'if')),
    (EmojiRep(tokenize.ERRORTOKEN, '⏩'), EmojiRep(None, 'pass')),
    (EmojiRep(tokenize.ERRORTOKEN, '🌍'), EmojiRep(None, 'global')),
    (EmojiRep(tokenize.ERRORTOKEN, '💔'), EmojiRep(None, 'break')),
    (EmojiRep(tokenize.ERRORTOKEN, '👍'), EmojiRep(bool, 'True')),
    (EmojiRep(tokenize.ERRORTOKEN, '👎'), EmojiRep(bool, 'False')),
    (EmojiRep(tokenize.ERRORTOKEN, '🇫🇷'), EmojiRep(None, 'yield')),
    (EmojiRep(tokenize.ERRORTOKEN, '🚫'), EmojiRep(None, 'None')),
    (EmojiRep(tokenize.ERRORTOKEN, '🐑'), EmojiRep(None, 'lambda')),
    (EmojiRep(tokenize.ERRORTOKEN, '🏫'), EmojiRep(None, 'class')),
    (EmojiRep(tokenize.ERRORTOKEN, '📥'), EmojiRep(None, 'import')),
    (EmojiRep(tokenize.ERRORTOKEN, '✌'), EmojiRep(None, 'try')),
    (EmojiRep(tokenize.ERRORTOKEN, '🎀'), EmojiRep(None, 'not')),

    (EmojiRep(tokenize.ERRORTOKEN, '🖨'), EmojiRep(None, 'print')),
]


class EmojiMapper:

    emojitopython = dict((key.val, item.val) for key, item in REPLACEMENTS)
    tupletoemoji = dict((item, key.val) for key, item in REPLACEMENTS)
    pythontoemoji = dict((item.val, key.val) for key, item in REPLACEMENTS)

    def __getitem__(self, item):
        # For treating an instance like a dict
        if isinstance(item, tuple):
            # If tuple convert to our namedtuple and pass
            return self.tupletoemoji[EmojiRep(*item)]
        else:
            # Otherwise attempt to read from both dicts
            try:
                return self.emojitopython[item]
            except KeyError:
                return self.pythontoemoji[item]

    def __contains__(self, item):
        # Same as getitem essentially
        if isinstance(item, tuple):
            if EmojiRep(*item) in self.tupletoemoji.keys():
                return True
            else:
                return False

        else:
            if item in self.emojitopython.keys() or item in self.pythontoemoji.keys():
                return True
            else:
                return False
