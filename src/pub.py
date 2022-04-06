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

    def buy_a_drink(self, name, customer):
        drink = self.find_drink_by_name(name)
        customer.reduce_money(drink.price)
        self.increase_till(drink.price)
 
    def can_drink(self, age):
        if age >= 18:
            return True
