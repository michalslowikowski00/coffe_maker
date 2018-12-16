

class CoffeeBeansTank:
    # TODO docstring
    amnt_of_coffee: int = 1000

    def get_coffee(self):
        return self.amnt_of_coffee

    def set_coffee(self, coffee):
        if coffee >= 100:
            self.amnt_of_coffee = coffee
        else:
            print("No coffee, please fill the coffee beans")
            return False


class WaterTank:
    # TODO docstring
    amnt_of_water: int = 1000

    def get_water(self):
        return self.amnt_of_water

    def set_water(self, water):
        if water >= 100:
            self.amnt_of_water = water
        else:
            print("No water, please fill the water tank")
            return False
