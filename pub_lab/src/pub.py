class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {}

    def increase_till(self, cash):
        self.till += cash

    def sell_drink_to_customer(self, drink, customer):
        if not customer.age >= 18:
            return False
        elif customer.drunkness_level >= 10:
            return False
        customer.reduce_cash(drink.price)
        self.increase_till(drink.price)
        customer.consume_drink(drink)
        #customer.add_drink(drink.name)

    def sell_food_to_customer(self, food, customer):
        customer.reduce_cash(food.price)
        self.increase_till(food.price)
        customer.consume_food(food)

    def add_drink_to_stock(self, drink):
        if drink.name not in self.drinks:
            self.drinks[drink.name] = {"quantity": 1, "price": drink.price}
        else:
            self.drinks[drink.name]["quantity"] += 1
        #breakpoint()

    # def stock_value(self):
    #     stock_value = 0
    #     for drink in self.drinks:
    #         stock_value += drink.price
    #     return stock_value