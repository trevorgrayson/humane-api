import os
import logging
from yaml import load, Loader
from .models import Feed

FEED_CONFIG = "/".join((os.environ.get("HOME", '.'), ".feeds/feeds.yml"))

# hash in dir to see if read.


def all_feeds():
    logging.info(f"Opening `{FEED_CONFIG}`...")
    config = load(open(FEED_CONFIG, 'r').read(), Loader=Loader)
    logging.info("OK.")

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


def get_feed(feeds=None):
    if feeds is None:
        feeds = all_feeds()

    for feed in feeds:
        feed = Feed(**feed)
        logging.info(f"Fetching {feed.url}")
        feed.fetch()

        for entry in feed.entries:
            print_line(entry)
