class Monetary:
    """Monetary units"""

    def __init__(self, amount, currency):
        """
        :param amount: amount of money
        :param currency: string
        """
        self.amount = float(amount)
        self.currency = currency

    def __eq__(self, other):
        if self.currency == other.currency:
            return self.amount == other.amount
        else:
            raise CurrenciesMismatchError(self.currency, other.currency)

    def __float__(self):
        return self.amount

    def __int__(self):
        return int(self.amount)

    def __lt__(self, other):
        if self.currency == other.currency:
            return self.amount < other.amount
        else:
            raise CurrenciesMismatchError(self.currency, other.currency)

    def __le__(self, other):
        if self.currency == other.currency:
            return self.amount <= other.amount
        else:
            raise CurrenciesMismatchError(self.currency, other.currency)

    def __add__(self, other):
        if self.currency == other.currency:
            return Monetary(self.amount + other.amount, self.currency)
        else:
            raise CurrenciesMismatchError(self.currency, other.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            return Monetary(self.amount - other.amount, self.currency)
        else:
            raise CurrenciesMismatchError(self.currency, other.currency)

    def __mul__(self, other):
        return Monetary(self.amount * other, self.currency)

    def __truediv__(self, other):
        return Monetary(self.amount / other, self.currency)

    def __pow__(self, exponent):
        return Monetary(self.amount ** exponent, self.currency)

    def __mod__(self, other):
        return Monetary(self.amount % other, self.currency)

    def __abs__(self):
        return Monetary(abs(self.amount), self.currency)

    def __repr__(self):
        return f'{self.amount:.2f}{self.currency}'


class CurrenciesMismatchError(Exception):
    """Error thrown when e.g. comparing or adding two Monetary with different currencies"""

    def __init__(self, currency1, currency2):
        """
        :param currency1: mismatched currency
        :param currency2: mismatched currency
        """
        super().__init__(f'Monetary values represented in different currencies: {currency1}, {currency2}')
