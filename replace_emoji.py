import tokenize
import hashlib
import csv
import unicodedata

DEBUG = False

EMOJI_NAMES = list(c['Name'] for c in
                   csv.DictReader(
                       open('./full-emoji-list.tsv'), delimiter='\t')
                   )


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

REPLACEMENTS = {
    (tokenize.ERRORTOKEN,   '⭐'): '*',
    (tokenize.ERRORTOKEN, '❔'): 'if',
    (tokenize.ERRORTOKEN, '⏩'): 'pass',
    (tokenize.ERRORTOKEN, '🌍'): 'global',
    (tokenize.ERRORTOKEN, '💔'): 'break',
    (tokenize.ERRORTOKEN, '👍'): 'True',
    (tokenize.ERRORTOKEN, '👎'): 'False',
    (tokenize.ERRORTOKEN, '🇫🇷'): 'yield',
    (tokenize.ERRORTOKEN, '🚫'): 'None',
    (tokenize.ERRORTOKEN, '🐑'): 'lambda',
    (tokenize.ERRORTOKEN, '🏫'): 'class',
    (tokenize.ERRORTOKEN, '📥'): 'import',
    (tokenize.ERRORTOKEN, '✌'): 'try',
    (tokenize.ERRORTOKEN, '🎀'): 'not',

    (tokenize.ERRORTOKEN, '🖨'): 'print', (tokenize.ERRORTOKEN, '📠'): 'print',
}

REVERSE_REPLACEMENTS = {
    (bool, 'True') : '👍',
    (bool, 'False') : '👎',
    (int, '0'): '0️⃣', 
    (int, '100'): '💯', 
}


def replace_keywords(token_list):
    for t in token_list:
        if (t.type, t.string) in REPLACEMENTS:
            yield tokenize.TokenInfo(
                type=t.type,
                string=REPLACEMENTS[(t.type, t.string)],
                start=t.start,
                end=t.end,
                line=t.line
            )
        else:
            yield t


def is_emoji(c):
    return unicodedata.name(c) in EMOJI_NAMES


def replace_names(token_list):
    '''
    Replace variable names which contain an emoji with the hash of the string
    '''
    for t in token_list:
        if t.type in (tokenize.ERRORTOKEN, tokenize.NAME) and any(map(is_emoji, t.string)):
            yield tokenize.TokenInfo(
                type=t.type,
                string='_' +
                hashlib.md5(t.string.encode('utf-8')).hexdigest(),
                start=t.start,
                end=t.end,
                line=t.line
            )
        else:
            yield t


def replace_emoji(token_list):
    token_list = replace_keywords(token_list)
    token_list = replace_names(token_list)
    token_list = list(token_list)
    if DEBUG:
        for token in token_list:
            print(token)
    return token_list


def output_formatter(arg, p = None, cycle=None):
    if p:
        if (type(arg), str(arg)) in REVERSE_REPLACEMENTS:
            return p.text(REVERSE_REPLACEMENTS[(type(arg), str(arg))])
        else:
            return p.text(str(arg))
    else:
        if (type(arg), str(arg)) in REVERSE_REPLACEMENTS:
            return REVERSE_REPLACEMENTS[(type(arg), str(arg))]
        else:
            return str(arg)

#  token_list = [
#      tokenize.TokenInfo(
#          type=tokenize.AT, string='@', start=None, end=None, line=None),
#      tokenize.TokenInfo(
#          type=tokenize.OP, string='⭐', start=None, end=None, line=None),
#      tokenize.TokenInfo(
#          type=tokenize.NAME, string='bar🍫', start=None, end=None, line=None),
#  ]
#  replace_emoji(token_list)
