

class CoffeeBeansTank:
    # TODO docstring
    amount_of_coffee: int = 1000
    '''
    r = dataBase
    amount_of_coffee: int = f.read(coffeeBeans)
    
    '''

    def get_coffee(self):
        return self.amount_of_coffee

    def set_coffee(self, coffee):
        if coffee >= 100:
            self.amount_of_coffee = coffee
        else:
            print("No coffee, please fill the coffee beans")
            return False


class WaterTank:
    # TODO docstring
    # Logic like in CoffeeBeansTank
    amount_of_water: int = 1000


class Sugar:
    amount_of_sugar = 1000


class Milk:
    amount_of_milk = 1000


def supply():
    file = open("/Users/negativeone/Documents/programming/python/cwiczenia/coffee_maker/supply.txt")
    print(file)


if __name__ == "__main__":
    supply()