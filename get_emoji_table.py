import os
import bs4
import re
import requests


def main():
    """
    Download emoji list from unicode.org and create a tabbed text output.
    """
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

    emojidata = list()

    for i, row in enumerate(table.find_all('tr')):
        rowdata = [c.text for c in row.find_all(re.compile('th|td'))]
        if i == 0 or rowdata[0] != '№':
            # We just want the emoji and the name
            emojidata.append((rowdata[2], rowdata[15]))

    with open(outpath, 'w', encoding='utf8') as out:
        for line in emojidata:
            out.write('\t'.join(line))
            out.write('\n')


if __name__ == '__main__':
    main()
