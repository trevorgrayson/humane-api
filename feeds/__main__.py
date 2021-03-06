import feeds
import yaml

if __name__ == "__main__":
    try:
        feeds.get_feed()
    except IOError as err:
        print("""
# `~/.feeds/feeds.yml` file was not found in your home directory.
# you may direct this message's output to the file to get started.
feeds:
  oss:
    - url: https://api.travis-ci.com/repos/trevorgrayson/pointillism/builds.atom
      status:
        summary: "(?<=State: )\\w+"
      group_by:
        title: "^[\\w\/]*"
  teamcity:
    - url: https://tc.rsci.co/httpAuth/feed.html?buildTypeId=...
      username: xxx
      password: yyy
      status: 
        title: "(?<=was )\\w+"
      group_by:
        title: "\\[.*\\]"
""")
#   news:
#     - url: https://feeds.a.dj.com/rss/RSSWorldNews.xml
#     - url: https://feeds.a.dj.com/rss/RSSWSJD.xml
#     - url: https://rss.nytimes.com/services/xml/rss/nyt/World.xml
#     - url: https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml
