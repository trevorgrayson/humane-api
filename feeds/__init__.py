import os
import feedparser
import os
from yaml import load, Loader
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

FEED_CONFIG = "/".join((os.environ.get("HOME", '.'), ".feeds/feeds.yml"))


def all_feeds():
    config = load(open(FEED_CONFIG, 'r').read(), Loader=Loader)

    for key, urls in config['feeds'].items():
        for url in urls:
            yield url


def get_feed():

    for feed in all_feeds():
        NewsFeed = feedparser.parse(feed)

        returns = {}

        for entry in NewsFeed.entries:
<<<<<<< HEAD
            project, status = entry.title.split('#')
            returns[project] = returns.get(project, [])   
            returns[project].append((entry.published, status, entry.link))

        # need a preview
        # need a method, returns tuple or string with params to print

        for ret, items in returns.items():
            row = max(items)

            output = (
                ret,
                '\t\t\t',
                row[2]
            )

            if ('success' not in row[1]):
                output = ('[x]',) + output
=======
            print(entry.title) # + " :: " + entry.published)
            print("\t" + entry.link)
            # print "\t" + entry.summary
>>>>>>> moving towards python3

                print(''.join(output))
            
