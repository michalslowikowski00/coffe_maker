""" Module with two types of coffee -- espresso and americano."""

from Coffee_Ingredient.ingredient import Ingredient
from Messeges.messages import Messages


class Coffee:

    # TODO: add ojects for coffee and water
    def make_coffee(self, bean, water):

        ingredient = Ingredient()

        if ingredient.Beans.amnt_of_coffee < bean:
            print("No coffee, please fill the coffee beans")
            return False
        if ingredient.Water.amnt_of_water < water:
            print("No water, please fill the water tank")
            return False
        # if ingredient.Beans.amnt_of_coffee and ingredient.Water.amnt_of_water < bean and water:
        #     print("No coffee, water, please fill ingr")
        #     return False
        print(Messages.checking_coffee)
        print(Messages.preparing_espresso)
        print(Messages.coffee_is_ready)
        # self.set_new_values_for_coffee_ingredients(Ingredient.Coffee.coffee_for_espresso)
        # self.set_new_values_for_water_ingredients(Ingredient.Coffee.water_for_espresso)
        return True


        # if ingredient.Beans.amnt_of_coffee and ingredient.Water.amnt_of_water < bean and water:
        #     print(Messages.no_water)
        #     return False
        # if ingredient.Water.amnt_of_water < coffe_ingredient:
        #     print(Messages.no_coffee)
        #     return False

class Espresso(Coffee):
    """  """

    def __init__(self, bean=15, water=150):
        self.bean = bean
        self.water = water


class Americano(Coffee):
    """  """

    def __init__(self, bean=10, water=250):
        self.bean = bean
        self.water = water
