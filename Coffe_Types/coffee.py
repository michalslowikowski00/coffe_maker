""" Module with two types of coffee -- espresso and americano."""

from Coffee_Ingredient.ingredient import Ingredient
from Messeges.messages import Messages


class Coffee:
    """Abstract class with one method for checking if
    coffee ingredients are available for preparing coffee.
    Method make_coffee returns boolean value."""

    @staticmethod
    def make_coffee(bean, water):
        ingredient = Ingredient()
        result = True

        if ingredient.Beans.amnt_of_coffee < bean:
            result = False
            print(Messages.no_coffee)
        if ingredient.Water.amnt_of_water < water:
            print(Messages.no_water)
            result = False
        if result:
            print(Messages.checking_coffee)
            print(Messages.preparing_coffee)
            print(Messages.coffee_is_ready)
            return result
        return result

        # todo: add set new values in this


class Espresso(Coffee):
    """Class with default values for bean and water used in CoffeeMaker"""

    def __init__(self, bean=15, water=150):
        self.bean = bean
        self.water = water


class Americano(Coffee):
    """Class with default values for bean and water used in CoffeeMaker"""

    def __init__(self, bean=10, water=250):
        self.bean = bean
        self.water = water
