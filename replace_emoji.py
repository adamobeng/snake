import tokenize
import hashlib
import csv
import unicodedata

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
#  try
#  while
#  with

REPLACEMENTS = {
    (tokenize.OP,   '⭐'): '*',
    (tokenize.NAME, '❔'): 'if',
    (tokenize.NAME, '❔⏩'): 'pass',
    (tokenize.NAME, '❔🌍'): 'global',
    (tokenize.NAME, '❔💔'): 'break',
    (tokenize.NAME, '❔👍'): 'True',
    (tokenize.NAME, '❔👎'): 'False',
    (tokenize.NAME, '🇫🇷'): 'yield',
    (tokenize.NAME, '🚫'): 'not',
    (tokenize.NAME, '🐑'): 'lambda',
    (tokenize.NAME, '🏫'): 'class',
    (tokenize.NAME, '📥'): 'import',
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
    for t in token_list:
        if t.type == tokenize.NAME:
            if any(map(is_emoji, t.string)):
                yield tokenize.TokenInfo(
                    type=t.type,
                    string='_' +
                    hashlib.md5(t.string.encode('utf-8')).hexdigest(),
                    start=t.start,
                    end=t.end,
                    line=t.line
                )
            break
        yield t


def replace_emoji(token_list):
    token_list = replace_keywords(token_list)
    token_list = replace_names(token_list)
    return list(token_list)


token_list = [
    tokenize.TokenInfo(
        type=tokenize.AT, string='@', start=None, end=None, line=None),
    tokenize.TokenInfo(
        type=tokenize.OP, string='⭐', start=None, end=None, line=None),
    tokenize.TokenInfo(
        type=tokenize.NAME, string='bar🍫', start=None, end=None, line=None),
]
replace_emoji(token_list)
