import os
from yaml import load, Loader
from .models import Feed

FEED_CONFIG = "/".join((os.environ.get("HOME", '.'), ".feeds/feeds.yml"))

# hash in dir to see if read.


def all_feeds():
    config = load(open(FEED_CONFIG, 'r').read(), Loader=Loader)

    for key, urls in config['feeds'].items():
        for url in urls:
            yield url


def print_line(entry):
    headline = [entry.title]

    if entry.status:
        headline.append(entry.status)

    headline.append(entry.timestamp)
    headline.append(entry.link)

    print("\t".join(headline))
    # print(entry.summary)


def get_feed():

    for feed in all_feeds():
        feed = Feed(**feed)
        feed.fetch()

        for entry in feed.entries:
            print_line(entry)
