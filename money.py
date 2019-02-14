class Monetary:
    """Monetary units"""

    def __init__(self, amount, currency):
        """
        :param amount: amount of money
        :param currency: string
        """
        self.amount = float(amount)
        self.currency = currency
