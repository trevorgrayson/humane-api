from sys import argv
from os import environ

from . import Robin

PORTFOLIO = f"{environ['HOME']}/.portfolio"

if __name__ == '__main__':
    if len(argv) > 2:
        stonks = argv[1:]
    else:
        stonks = []
        with open(PORTFOLIO, 'r') as portfolio:
            for line in portfolio:
                stonks.append(line.strip())

    rh = Robin()

    print(rh.quote(stonks))

