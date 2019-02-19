import csv

import requests

from money import Monetary


class FixedRateConverter:

    def __init__(self):
        self.rates = {
            'EUR': {
                'EUR': 1,
                'PLN': 4.3382,
                'USD': 1.1268
            },
            'USD': {
                'EUR': 0.8854,
                'PLN': 3.8371,
                'USD': 1
            }
        }

    def import_rates_from_csv(self, file_path):
        with open(file_path, 'r') as csv_file:
            self.rates = {}
            reader = csv.DictReader(csv_file)
            for row in reader:
                base = row['Base']
                currency = row['Currency']
                rate = float(row['Rate'])
                if base not in self.rates:
                    self.rates[base] = {}
                self.rates[base][currency] = rate

    def convert(self, from_monetary, to_currency):
        """
        Convert monetary to different currency

        :param from_monetary: the monetary unit to be converted
        :param to_currency: target currency
        :return: Monetary unit of target currency
        """
        try:
            rate = self.rates[from_monetary.currency][to_currency]
            return Monetary(from_monetary * rate, to_currency)
        except KeyError:
            raise ExchangeRateNotDefined(from_monetary.currency, to_currency)


class DynamicRateConverter(FixedRateConverter):
    """RateExchangeConverter using rates from https://api.exchangeratesapi.io"""
    api_url = 'https://api.exchangeratesapi.io'

    def __init__(self):
        super().__init__()
        self.rates = {}
        self.import_rates_from_api('EUR')
        self.import_rates_from_api('USD')

    def import_rates_from_api(self, base_currency):
        response = requests.get(f'{self.api_url}/latest/?base={base_currency}')
        response_dict = response.json()
        self.rates[base_currency] = {}
        for to_currency, rate in response_dict['rates'].items():
            self.rates[base_currency][to_currency] = rate


class ExchangeRateNotDefined(Exception):

    def __init__(self, from_currency, to_currency):
        super().__init__(f'Exchange rate {from_currency} to {to_currency} is not defined')
