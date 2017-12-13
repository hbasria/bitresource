import unittest

from bitresource.blockchain import ExchangeRates


class TestBlockChainInfoResources(unittest.TestCase):

    def test_exchange_rates(self):
        rates = list(ExchangeRates.data())

        self.assertEqual(rates[0].code, 'BTC')


if __name__ == '__main__':
    unittest.main()
