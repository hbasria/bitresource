import os

from coinbase.models import AccountObject, PaymentMethodObject
from http_resource import HttpResource

HTTP_RESOURCES = {
    'default': {
        'endpoint_url': 'https://api.coinbase.com/v2/',
        'api_key': 'DTGIxEEFZGVx5Wui',
        'api_secret': 'KhyjAv9PFvsJP3SKxQaBcv4gTqjySWjE',
        'api_version': '2017-09-14',
        'auth': 'coinbase.auth.HMACAuth'

    }
}

os.environ.setdefault('HTTP_RESOURCES', str(HTTP_RESOURCES))

Currency = HttpResource('currencies')
ExchangeRates = HttpResource('exchange-rates')
Account = HttpResource('accounts', api_object=AccountObject)



PaymentMethod = HttpResource('payment-methods', api_object=PaymentMethodObject)


class PriceResource(HttpResource):

    def buy(self, *args, **params):
        if 'currency_pair' in params:
            currency_pair = params['currency_pair']
        else:
            currency_pair = 'BTC-USD'

        return self.query(*(currency_pair, 'buy'), **params)

    def sell(self, *args, **params):
        if 'currency_pair' in params:
            currency_pair = params['currency_pair']
        else:
            currency_pair = 'BTC-USD'

        return self.query(*(currency_pair, 'sell'), **params)

prices = PriceResource('prices')
# accounts = Account.query()
#
# for i in accounts.data:
#     for addr in i.get_addresses():
#         print(addr)


buy_rice = prices.buy(currency_pair='BTC-USD')
sell_rice = prices.sell(currency_pair='BTC-USD')

print(buy_rice, sell_rice)
