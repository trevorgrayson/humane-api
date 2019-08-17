import os
import feedparser
import os
import re
from yaml import load, Loader
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

FEED_CONFIG = "/".join((os.environ.get("HOME", '.'), ".feeds/feeds.yml"))

# hash in dir to see if read.

class Feed:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.status = kwargs.get('status')


    def fetch(self):
        self.entries = []

        self.NewsFeed = feedparser.parse(self.url)
        for entry in self.NewsFeed.entries:
            status_regex = re.compile(self.status, re.MULTILINE)
            status_match = re.search(status_regex, entry.summary)

            status = status_match[0] if status_match else 'unkwn'

            self.entries.append(Entry(
              title=entry.title,
              status=status,
              link=entry.link,
              timestamp=entry.updated
            ))

            if self.latest_only:
                break


    @property
    def latest_only(self):
        return self.status is not None


class Entry:
    def __init__(self, **kwargs):
        self.title=kwargs.get('title')
        self.status=kwargs.get('status')
        self.link=kwargs.get('link')
        self.timestamp=kwargs.get('timestamp')


    def __str__(self):
        build_success = re.compile("State: passed", re.MULTILINE)

        return entry.title + "\n" +\
            ("PASS" if re.search(build_success, entry.summary) else "FAIL") +\
            "\t" + entry.link
            # print "\t" + entry.summary




def all_feeds():
    config = load(open(FEED_CONFIG, 'r').read(), Loader=Loader)

    for key, urls in config['feeds'].items():
        for url in urls:
            yield url


def get_feed():

    for feed in all_feeds():
        feed = Feed(**feed)
        feed.fetch()

<<<<<<< HEAD
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
=======
        for entry in feed.entries:
            print(f"{entry.title} :: {entry.status} :: {entry.timestamp}")
            # print(entry.summary)
>>>>>>> feeds modeling
            print("\t" + entry.link)
            # print "\t" + entry.summary
>>>>>>> moving towards python3

                print(''.join(output))
            
