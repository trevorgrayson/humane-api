from pyrh import Robinhood
from os import environ


class Robin:
    def __init__(self):
        self.client = Robinhood()
        self.client.login(
            username=environ['RH_USERNAME'],
            password=environ['RH_PASSWORD']
        )

    def quote(self, symbols):
        """
        param symbols: array of tickers
        """
        return self.client.quote_datas(symbols)
