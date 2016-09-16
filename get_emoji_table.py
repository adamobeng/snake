import os
import bs4
import re
import requests


outpath = 'full-emoji-list.tsv'
emojihtml = 'full-emoji-list.html'
emojiurl = 'http://unicode.org/emoji/charts/full-emoji-list.html'

if not os.path.isfile(emojihtml):
    do_download = input("Emoji list not found, download from unicode.org (~26mb)? (y/N)")
    if do_download.lower() == 'y':
        emojireq = requests.get(emojiurl)
        with open(emojihtml, 'wb') as op:
            op.write(emojireq.content)

soup = bs4.BeautifulSoup(open(emojihtml, encoding='utf8'), 'html.parser')
table = soup.find_all('table')[0]

out = open(outpath, 'w', encoding='utf8')
for row in table.find_all('tr'):
    out.write(
            '\t'.join([c.text for c in row.find_all(re.compile('th|td'))]) + '\n'
    )
