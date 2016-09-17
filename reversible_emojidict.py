import types
import tokenize
from collections import namedtuple


# Keywords to Replace
#  None
#  and
#  as
#  assert
#  continue
#  def
#  del
#  elif
#  else
#  except
#  finally
#  for
#  from
#  in
#  is
#  nonlocal
#  not
#  or
#  raise
#  return
#  while
#  with


EmojiRep = namedtuple('EmojiReplacement', ['type', 'val'])


REPLACEMENTS_DATA = [
    # Keywords
    (EmojiRep(tokenize.ERRORTOKEN, '⭐'), EmojiRep(None, '*')),
    (EmojiRep(tokenize.ERRORTOKEN, '❔'), EmojiRep(None, 'if')),
    (EmojiRep(tokenize.ERRORTOKEN, '⏩'), EmojiRep(None, 'pass')),
    (EmojiRep(tokenize.ERRORTOKEN, '🌍'), EmojiRep(None, 'global')),
    (EmojiRep(tokenize.ERRORTOKEN, '💔'), EmojiRep(None, 'break')),
    (EmojiRep(tokenize.ERRORTOKEN, '👍'), EmojiRep(bool, 'True')),
    (EmojiRep(tokenize.ERRORTOKEN, '👎'), EmojiRep(bool, 'False')),
    (EmojiRep(tokenize.ERRORTOKEN, '🇫🇷'), EmojiRep(None, 'yield')),
    (EmojiRep(tokenize.ERRORTOKEN, '🚫'), EmojiRep(type(None), 'None')),
    (EmojiRep(tokenize.ERRORTOKEN, '🐑'), EmojiRep(None, 'lambda')),
    (EmojiRep(tokenize.ERRORTOKEN, '🏫'), EmojiRep(None, 'class')),
    (EmojiRep(tokenize.ERRORTOKEN, '📥'), EmojiRep(None, 'import')),
    (EmojiRep(tokenize.ERRORTOKEN, '🙏'), EmojiRep(None, 'try')),
    (EmojiRep(tokenize.ERRORTOKEN, '🎀'), EmojiRep(None, 'not')),
    (EmojiRep(tokenize.ERRORTOKEN, '🍀'), EmojiRep(None, 'for')),
    (EmojiRep(tokenize.ERRORTOKEN, '👩‍👩‍👧‍👦'), EmojiRep(type, 'set')),
    (EmojiRep(tokenize.ERRORTOKEN, '👇'), EmojiRep(None, 'in')),
    (EmojiRep(tokenize.ERRORTOKEN, '🤘'), EmojiRep(None, 'finally')),

    # Built-in Functions
    (EmojiRep(tokenize.ERRORTOKEN, '📖'), EmojiRep(type(open), 'open')),

    (EmojiRep(tokenize.ERRORTOKEN, '🖨'), EmojiRep(type(print), 'print')),
    (EmojiRep(tokenize.ERRORTOKEN, '⬅'), EmojiRep(None, '=')),
    (EmojiRep(tokenize.ERRORTOKEN, '◀'), EmojiRep(None, '=')),

    # Comparison Operators

    # Class Methods
    (EmojiRep(tokenize.ERRORTOKEN, '📕'), EmojiRep(type(open), 'close')),

    # Additional Esoteric
    (EmojiRep(tokenize.ERRORTOKEN, '🐱'), EmojiRep(types.FunctionType, 'cat')),
]


class EmojiMapper:

    emojitopython = dict((key.val, item.val) for key, item in REPLACEMENTS_DATA)
    tupletoemoji = dict((item, key.val) for key, item in REPLACEMENTS_DATA)
    tupletopython = dict((key, item.val) for key, item in REPLACEMENTS_DATA)
    pythontoemoji = dict((item.val, key.val) for key, item in REPLACEMENTS_DATA)

    def __getitem__(self, item):
        # For treating an instance like a dict
        if isinstance(item, tuple):
            # If tuple convert to our namedtuple and pass
            try:
                return self.tupletoemoji[EmojiRep(*item)]
            except KeyError:
                return self.tupletopython[EmojiRep(*item)]
        else:
            # Otherwise attempt to read from both dicts
            try:
                return self.emojitopython[item]
            except KeyError:
                return self.pythontoemoji[item]

    def __contains__(self, item):
        # Same as getitem essentially
        if isinstance(item, tuple):
            if EmojiRep(*item) in self.tupletoemoji.keys() or EmojiRep(*item) in self.tupletopython.keys():
                return True
            else:
                return False
        else:
            if item in self.emojitopython.keys() or item in self.pythontoemoji.keys():
                return True
            else:
                return False
