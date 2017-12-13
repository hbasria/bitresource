import unittest

from bitresource.bitpay import ExchangeRates, Currencies


class TestBitPayResources(unittest.TestCase):
    def test_exchange_eates(self):
        rates = list(ExchangeRates.data())

        self.assertEqual(rates[0].code, 'BTC')


if __name__ == '__main__':
    unittest.main()
