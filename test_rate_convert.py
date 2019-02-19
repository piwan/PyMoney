from money import Monetary
from rate_convert import FixedRateConverter, ExchangeRateNotDefined, DynamicRateConverter

converter = FixedRateConverter()
print(converter.convert(Monetary(10, "USD"), "EUR"))
print(converter.convert(Monetary(10, "USD"), "USD"))
try:
    print(converter.convert(Monetary(10, "USD"), "GHD"))
except ExchangeRateNotDefined as error:
    print(error)

converter.import_rates_from_csv('exchange_rates.csv')
print(converter.convert(Monetary(10, "USD"), "EUR"))
print(converter.convert(Monetary(10, "USD"), "USD"))

converter = DynamicRateConverter()
print(converter.convert(Monetary(10, "USD"), "EUR"))
print(converter.convert(Monetary(10, "USD"), "USD"))
print(converter.convert(Monetary(10, "USD"), "GBP"))