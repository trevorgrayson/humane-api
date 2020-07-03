import logging
import re
from feeds import Feed, get_feed
from time import sleep
import time

from collections import defaultdict

FEEDS = [
    {'url': 'https://feeds.npr.org/510318/podcast.xml'},
    {'url': 'https://feeds.npr.org/510289/podcast.xml'},
    {'url': 'https://feeds.npr.org/510325/podcast.xml'},
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


if __name__ == '__main__':

    for params in FEEDS:
        feed = Feed(**params)
        logging.info(feed)
        feed.fetch()

        for entry in feed.entries:
            print(" ".join((
                entry.title,
                )))
