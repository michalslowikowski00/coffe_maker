""" Module with two types of coffee -- espresso and americano."""

from Coffee_Ingredient.ingredient import Ingredient
from Messeges.messages import Messages


class Coffee:

    # TODO: add ojects for coffee and water
    def make_coffee(self, bean, water):

        ingredient = Ingredient()

        if ingredient.Beans.amnt_of_coffee and ingredient.Water.amnt_of_water < bean and water:
            print(Messages.no_water)
            return False
        # if ingredient.Water.amnt_of_water < coffe_ingredient:
        #     print(Messages.no_coffee)
        #     return False


class Espresso(Coffee, Ingredient.Coffee, Ingredient.Beans, Ingredient.Water):
    """  """

    def __init__(self, bean=15, water=150):
        self.bean = bean
        self.water = water


class Americano(Coffee, Ingredient.Coffee, Ingredient.Beans, Ingredient.Water):
    """  """

    def __init__(self, bean=10, water=250):
        self.bean = bean
        self.water = water
