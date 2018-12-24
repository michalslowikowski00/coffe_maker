""" Module with two types of coffee -- espresso and americano."""

from coffe_ingredients import CoffeeBeansTank, WaterTank
from messages import Messages


class Coffee(CoffeeBeansTank, WaterTank):
    """ Class with two methods -- espresso & americano.
        Four attributes which are coffee ingredients, values are integers.
        Attributes are used in both methods. """

    # def __init__(self, coffee, water):
    #     self.coffee = coffee   # take value from database?
    #     self.water = water    # take value from database?

    water_for_espresso: int = 100
    coffee_for_espresso: int = 15
    water_for_americano: int = 250
    coffee_for_americano: int = 10


class Espresso(Coffee):
    """  """

    def espresso(self):
        """ Method will check if amount of water or coffee is available in water or coffee tanks.
         Method will return False if one these ingredients is low than expected.
         Type of both ingredients -- water & coffee are integers.
         True will be return if both ingredients are enough.
         Messages are taken from Messages module."""

        if self.amnt_of_water < self.water_for_espresso:
            print(Messages.no_water)
            return False
        if self.amnt_of_coffee < self.coffee_for_espresso:
            print(Messages.no_coffee)
            return False
        return True


class Americano(Coffee):
    """  """

    def americano(self):
        """ Method will check if amount of water or coffee is available in water or coffee tanks.
         Method will return False if one these ingredients is low than expected.
         Type of both ingredients -- water & coffee are integers.
         True will be return if both ingredients are enough.
         Messages are taken from Messages module. """

        if self.amnt_of_water < self.water_for_americano:
            print(Messages.no_water)
            return False
        if self.amnt_of_coffee < self.coffee_for_americano:
            print(Messages.no_coffee)
            return False
        return True
