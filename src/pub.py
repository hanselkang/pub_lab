class Pub:
    def __init__(self, input_name, input_till, drink):
        self.name = input_name
        self.till = input_till
        self.drink = drink

    def find_drink_by_name(self, name):
        for drink in self.drink:
            if drink.name == name:
                return drink

    def increase_till(self, amount):
        self.till += amount

    def can_drink(self, customer):
        return customer.age >= 18

        
    def check_drunkenness(self, customer):
        not_drunk = True
        if customer.drunkenness > 5:
            not_drunk = False
        return not_drunk

    def buy_a_drink(self, name, customer):
        self.can_drink(customer)
        self.check_drunkenness(customer)
        drink = self.find_drink_by_name(name)
        customer.reduce_money(drink.price)
        self.increase_till(drink.price)
        customer.drunkenness += drink.alcohol_level
 

