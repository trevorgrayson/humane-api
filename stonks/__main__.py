import logging
from time import sleep
from feeds import Feed, get_feed
from . import FEEDS, REG_EXP, TICKER_BLACK_LIST, save_hashed

if __name__ == '__main__':

    for params in FEEDS:
        feed = Feed(**params)
        logging.info(feed)
        feed.fetch()
        sleep(3)

        lips = {}
        lines = []
        for entry in feed.entries:
            matches = REG_EXP.findall(entry.content)
            uniques = sorted(set(matches).difference(TICKER_BLACK_LIST))
            for unique in uniques:
                lips[unique] = lips.get(unique, 0) + 1
            line = ", ".join(map(str, (
                entry.timestamp, len(uniques), "  ".join(uniques)
            )))
            print(line)
            lines.append(line)
        save_hashed(lines, 'wallstreetbets', 'posts')

        top_ten = sorted(lips, key=lips.__getitem__, reverse=True)[0:10]
        print(f"TOP TEN (User Mention Count):")
        lines = []
        for top in top_ten:
            line = f"{top}: {lips[top]}"
            print(line)
            lines.append(line)
        save_hashed(lines, 'wallstreetbets', 'top_ten')
