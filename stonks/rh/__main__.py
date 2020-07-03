from sys import argv

from . import Robin

if __name__ == '__main__':
    rh = Robin()

    rh.quote(argv[1:])
