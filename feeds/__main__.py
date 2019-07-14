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
  news:
    - https://feeds.a.dj.com/rss/RSSWorldNews.xml
    - https://feeds.a.dj.com/rss/RSSWSJD.xml
    - https://rss.nytimes.com/services/xml/rss/nyt/World.xml
    - https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml
""")
