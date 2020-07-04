from pyrh import Robinhood, dump_session, load_session, exceptions
from os import environ

KEYS = ['symbol', 'last_trade_price']


def drint(obj, *keys):
    out = []
    for key in keys:
        out.append(obj.get(key))
    return "\t".join(map(str, out))


class Robin:
    def __init__(self):
        try:
            self.client = load_session()
        except exceptions.InvalidCacheFile:
            self.client = Robinhood(
                username=environ['RH_USERNAME'],
                password=environ['RH_PASSWORD']
            )
            dump_session(self.client)

    def quote(self, symbols):
        """
        param symbols: array of tickers
        """
        print("\t".join(KEYS))
        for sym in self.client.quotes_data(symbols):
            if sym is not None:
                print(drint(sym, *KEYS))
