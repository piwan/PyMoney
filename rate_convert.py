import csv

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


class ExchangeRateNotDefined(Exception):

    def __init__(self, from_currency, to_currency):
        super().__init__(f'Exchange rate {from_currency} to {to_currency} is not defined')
