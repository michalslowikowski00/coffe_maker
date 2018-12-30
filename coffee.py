""" Module with two types of coffee -- espresso and americano."""

from ingredients import Ingredients
from messages import Messages


class Coffee:
    """ Class with two methods -- espresso & americano.
        Four attributes which are coffee ingredients, values are integers.
        Attributes are used in both methods. """

    water_for_espresso: int = 100
    coffee_for_espresso: int = 15
    water_for_americano: int = 250
    coffee_for_americano: int = 10


class Espresso(Coffee, Ingredients.CoffeeBeansTank, Ingredients.WaterTank): # import ingredients
    """  """

    def espresso(self):
        """ Method will check if amount of water or coffee is available in water or coffee tanks.
         Method will return False if one these ingredients is low than expected.
         Type of both ingredients -- water & coffee are integers.
         True will be return if both ingredients are enough.
         Messages are taken from Messages module."""

        # amnt_of_water id from ingredients
        if self.amnt_of_water < self.water_for_espresso:
            print(Messages.no_water)
            return False
        if self.amnt_of_coffee < self.coffee_for_espresso:
            print(Messages.no_coffee)
            return False
        return True


class Americano(Coffee, Ingredients.CoffeeBeansTank, Ingredients.WaterTank):
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
