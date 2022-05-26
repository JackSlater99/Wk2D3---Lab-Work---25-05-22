class Customer:
    def __init__(self, name, cash, age, drunkness_level = 0):
        self.name = name
        self.cash = cash
        self.age = age
        self.drunkness_level = drunkness_level
        # self.drinks = []
    
    # def add_drink(self, new_drink):
    #     self.drinks.append(new_drink)

    def reduce_cash(self, cash_value):
        self.cash -= cash_value
    
    def consume_drink(self, drink):
        self.drunkness_level += drink.alcohol_level

    def consume_food(self, food):
        self.drunkness_level -= food.rejuvination_level