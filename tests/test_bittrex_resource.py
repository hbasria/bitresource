import unittest

from bitresource.bittrex import Currency, Market, ExchangeRate


class TestBittrexResources(unittest.TestCase):

    def test_currency(self):
        currencies = list(Currency.data())
        currency_btc = [currency for currency in currencies if currency.Currency == 'BTC'][0]

        self.assertEqual(currency_btc.Currency, 'BTC')

    def test_market(self):
        markets = list(Market.data())
        market_eth = [market for market in markets if market.MarketName == 'BTC-ETH'][0]

        self.assertEqual(market_eth.MarketName, 'BTC-ETH')

    def test_exchange_rate(self):
        exchange_rate = ExchangeRate.data(market='BTC-ETH').first()

        self.assertListEqual(sorted(list(exchange_rate.keys())), ['Ask', 'Bid', 'Last'])


if __name__ == '__main__':
    unittest.main()
