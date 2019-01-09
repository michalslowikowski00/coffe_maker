""" Module with two types of coffee -- espresso and americano."""

from Coffee_Ingredients.ingredients import Ingredients
from Messeges.messages import Messages


class Coffee:

    def make_coffee(self):
        pass


class Espresso(Coffee, Ingredients.Coffee, Ingredients.Beans, Ingredients.Water):
    """  """

    def __init__(self, bean=15, water=150):
        self.bean = bean
        self.water = water

    def make_espresso(self):
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
        return self.make_coffee()


class Americano(Coffee, Ingredients.Coffee, Ingredients.Beans, Ingredients.Water):
    """  """

    def __init__(self, bean=10, water=250):
        self.bean = bean
        self.water = water

    def make_americano(self):
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
        return self.make_coffee()
