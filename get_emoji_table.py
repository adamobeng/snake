import bs4
import re

outpath = 'full-emoji-list.tsv'

soup = bs4.BeautifulSoup(open('snake/full-emoji-list.html'))
table = soup.find_all('table')[0]

out = open(outpath, 'w')
for row in table.find_all('tr'):
    out.write(
            '\t'.join([c.text for c in row.find_all(re.compile('th|td'))]) + '\n'
    )
