""" Module with two types of coffee -- espresso and americano."""

from ingredient.ingredient import Ingredient
from exception.custom_exception import Message, NoBeanError, NoWaterError


class Coffee:
    """Abstract class with one method for checking if
    coffee ingredients are available for preparing coffee.
    Method make_coffee returns boolean value.
    Method returns """

    bean = None
    water = None

    def make_coffee(self, bean, water):
        i = Ingredient()
        result = True

        while result:
            try:
                if i.bean <= bean:
                    result = False
                    raise NoBeanError
                if i.water <= water:
                    result = False
                    raise NoWaterError
            except NoBeanError:
                print(NoBeanError.no_coffee_message)
            except NoWaterError:
                print(NoWaterError.no_water_message)
            else:
                result = True
                print(Message.checking_coffee_message)
                print(Message.preparing_coffee_message)
                print(Message.coffee_is_ready_message)
            return result
            # todo: add set new values in this


class Espresso(Coffee):
    """Class which is Espresso object.
    Espresso has default values for bean and water.
    Values are integer."""

    def __init__(self, bean=15, water=150):
        self.bean = bean
        self.water = water


class Americano(Coffee):
    """Class which is Americano object.
        Americano has default values for bean and water.
        Values are integer.
        @param: integer"""

    def __init__(self, bean=10, water=250):
        self.bean = bean
        self.water = water
