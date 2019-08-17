import re
import feedparser


# source
class Feed:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.status = kwargs.get('status')


    def fetch(self):
        self.entries = []

        self.NewsFeed = feedparser.parse(self.url)
        for entry in self.NewsFeed.entries:
            self.entries.append(Entry(
              title=entry.title,
              summary=entry.summary,
              status=self.get_status(entry),
              link=entry.link,
              timestamp=entry.updated
            ))

            if self.latest_only:
                break

    def get_status(self, entry):
        if self.status:
            status_regex = re.compile(self.status, re.MULTILINE)
            status_match = re.search(status_regex, entry.summary)

            return status_match[0] if status_match else 'unkwn'


    @property
    def latest_only(self):
        return self.status is not None


class Entry:
    def __init__(self, **kwargs):
        self.title=kwargs.get('title')
        self.summary=kwargs.get('summary')
        self.status=kwargs.get('status')
        self.link=kwargs.get('link')
        self.timestamp=kwargs.get('timestamp')


    def __str__(self):
        build_success = re.compile("State: passed", re.MULTILINE)

        return entry.title + "\n" +\
            ("PASS" if re.search(build_success, entry.summary) else "FAIL") +\
            "\t" + entry.link
            # print "\t" + entry.summary
