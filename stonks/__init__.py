import re
import time

FEEDS = [
    {'url': 'https://www.reddit.com/r/wallstreetbets.rss'}
]

TICKER_BLACK_LIST = set(['FUCK', 'SHIT', 'SARS'])

REG_EXP = re.compile('[A-Z][A-Z][A-Z]?[A-Z]?[A-Z]?')
# TODO, this should be fed URLs


def save_hashed(data, root, prefix=None):
    # TODO automake dir
    date = time.strftime("%Y%m%d-%H%M")
    file = [date]
    if prefix is not None:
        file = [prefix] + file
    filename = f'data/stonks/{root}/{"-".join(file)}'

    with open(filename, 'w') as out:
        for line in data:
            out.write(line + "\n")


