import feedparser
from yaml import load, Loader

FEED_CONFIG = "/Users/tgrayson/.feeds/feeds.yml"


def all_feeds():
    config = load(open(FEED_CONFIG, 'r').read(), Loader=Loader)

    for key, urls in config['feeds'].iteritems():
        for url in urls:
            yield url


def get_feed():

    for feed in all_feeds():
        NewsFeed = feedparser.parse(feed)

        for entry in NewsFeed.entries:
            print entry.title + " :: " + entry.published  
            print "\t" + entry.link
            # print "\t" + entry.summary

