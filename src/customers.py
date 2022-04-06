class Customers:
    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet

    def reduce_money(self, amount):
        self.wallet -= amount

    