from Exception.custom_exception import NoCoffee, NoWater


class Ingredient: #abstrakcja

    # ile jest
    # ile potrezba
    # jaki ejst przepis
    #

    class Beans:
        # TODO docstring
        amnt_of_coffee: int = 1000

        def get_coffee(self):
            return self.amnt_of_coffee

        # if _i.Beans.amnt_of_coffee <= bean:
        #     _result = False
        #     raise NoCoffee
        # if _i.Water.amnt_of_water <= water:
        #     _result = False
        #     raise NoWater

        def set_coffee(self, coffee):
            if coffee >= 100:
                self.amnt_of_coffee = coffee
            else:
                raise NoCoffee("Amount of Coffee in class Beans: {0}".format(self.amnt_of_coffee))

    class Water:
        # TODO docstring
        amnt_of_water = 1000

        def get_water(self):
            return self.amnt_of_water

        def set_water(self, water):
            if water >= 100:
                self.amnt_of_water = water
            else:
                raise NoWater("Amount of Water in class Water: {0}".format(self.amnt_of_water))

    class NewIngredients(Beans, Water):
        def set_new_values_for_coffee_ingredients(self, amnt_coffee):
            # TODO doc string
            new_value_for_coffee = self.get_coffee() #amntofcoffe
            new_value_for_coffee -= amnt_coffee
            self.set_coffee(new_value_for_coffee)

        def set_new_values_for_water_ingredients(self, amnt_water):
            # TODO doc string
            new_value_for_water = self.get_water()
            new_value_for_water -= amnt_water
            self.set_water(new_value_for_water)
