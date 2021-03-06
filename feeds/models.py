import re
import random
import feedparser
import logging
import pdb
import requests
import urllib.request as urllib2
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# logging.basicConfig(level=logging.DEBUG) # filename='example.log',
logger = logging.getLogger(__name__)


# source
class Feed:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.status = kwargs.get('status')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.group_by = kwargs.get('group_by')

    def fetch(self):
        args = {
            'headers': {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
            }
        }

        creds = self.get_credentials()
        if creds:
            args['auth'] = creds

        # logger.info(f"fetching {self.url}")
        # pdb.set_trace()
        response = requests.get(self.url, **args,)
        if response.status_code != 200:
            raise Exception(f"HTTP: {response.status_code}: {response.text}")
        self.parse(response.text)

    def parse(self, text):
        self.entries = []
        self.NewsFeed = feedparser.parse(text)

        # logger.info(self.NewsFeed)
        logger.info(f"received {len(self.NewsFeed.entries)} entries")

        rows = {}
        for entry in self.NewsFeed.entries:
            if self.group_by:
                for k, v in self.group_by.items():
                    regex = re.compile(v, re.MULTILINE)
                    matches = re.search(regex, getattr(entry, k))

                    if matches:
                        hash_key = matches[0]
                        rows[hash_key] = rows.get(hash_key) or entry
            else:
                rows[random.random()] = entry

        for k, entry in rows.items():
            self.entries.append(Entry(
              title=entry.title,
              summary=entry.summary,
              status=self.get_status(entry),
              link=entry.link,
              enclosure=self.get_enclosures(entry),
              timestamp=entry.updated
            ))

    def get_enclosures(self, entry):
        if len(entry.enclosures) > 0:
            return entry.enclosures[0]['url']

    def get_status(self, entry):
        if self.status:
            for k, v in self.status.items():
                status_regex = re.compile(v, re.MULTILINE)
                status_match = re.search(status_regex, getattr(entry, k))

                return status_match[0] if status_match else 'unkwn'

    def get_credentials(self):
        if self.username:
            return (self.username, self.password)


class Entry:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.summary = kwargs.get('summary')
        self.content = kwargs.get('content', self.summary)
        self.status = kwargs.get('status')
        self.enclosure = kwargs.get('enclosure')
        self.link = kwargs.get('link')
        self.timestamp = kwargs.get('timestamp', kwargs.get('updated'))

    def __str__(self):
        build_success = re.compile("State: passed", re.MULTILINE)

        return self.title + "\n" +\
            ("PASS" if re.search(build_success, self.summary) else "FAIL") +\
            "\t" + self.link +\
            "\t" + self.summary + "\n"
