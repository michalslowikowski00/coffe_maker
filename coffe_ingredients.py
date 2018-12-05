from pprint import pprint


class CoffeeBeansTank:
    amount_of_coffee: int = 1000

    def getCoffee(self):
        return self.amount_of_coffee

    def setCoffee(self, coffee):
        if coffee >= 100:
            self.amount_of_coffee = coffee
        else:
            pprint("No coffee, please fill the coffee beans")
            return False


class WaterTank:
    amount_of_water: int = 1000

    def getWater(self):
        return self.amount_of_water

    def setWater(self, water):
        if water >= 250:
            self.amount_of_water = water
        else:
            pprint("No water, please fill the water")
            return False


class Sugar:
    amount_of_sugar = 1000


class Milk:
    amount_of_milk = 1000
