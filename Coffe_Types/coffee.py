""" Module with two types of coffee -- espresso and americano."""

from Coffee_Ingredient.ingredient import Ingredient
from Exception.custom_exception import Message, NoWater
from Exception.custom_exception import NoCoffee


class Coffee:
    """Abstract class with one method for checking if
    coffee ingredients are available for preparing coffee.
    Method make_coffee returns boolean value."""

    @staticmethod
    def make_coffee(bean, water):
        i = Ingredient()
        result = True

        while result:
            try:
                if i.Beans.amnt_of_coffee < bean:
                    result = False
                    raise NoCoffee
                if i.Water.amnt_of_water < water:
                    result = False
                    raise NoWater
            except NoCoffee:
                print(NoCoffee.no_coffee_message)
            except NoWater:
                print(NoWater.no_water_message)
            else:
                result = True
                print(Message.checking_coffee_message)
                print(Message.preparing_coffee_message)
                print(Message.coffee_is_ready_message)
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
