import requests
import json
from config import keys
class APIException(Exception):
    pass

class ValueConverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_t = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            quote_t = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        r = requests.get('http://data.fixer.io/api/latest?access_key=0f55eef4a61508ec1b549df88eeed941')
        total_base = float(json.loads(r.content)['rates'][quote_t]) / float(json.loads(r.content)['rates'][base_t])
        total_base *= float(amount)
        return total_base
