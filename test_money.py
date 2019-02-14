from money import Monetary, CurrenciesMismatchError

amount1 = Monetary(12, "PLN")

print(amount1)
print(amount1 > Monetary(1, "PLN"))
print(amount1 + Monetary(13, "PLN") * 2 - Monetary(10, "PLN") / 2)
print(Monetary(-2, "PLN") ** 3)
print(Monetary(10, "PLN") % 3)

try:
    Monetary(12, "PLN") + Monetary(13, "USD")
except CurrenciesMismatchError as e:
    print(e)
