from Exception.custom_exception import NoCoffee


class Ingredient:

    class Coffee:
        """ Class with two methods -- espresso & americano.
            Four attributes which are coffee ingredients, values are integers.
            Attributes are used in both methods. """

        water_for_espresso: int = 100
        coffee_for_espresso: int = 15
        water_for_americano: int = 250
        coffee_for_americano: int = 10

    class Beans:
        # TODO docstring
        amnt_of_coffee: int = 0

        def get_coffee(self):
            return self.amnt_of_coffee

        def set_coffee(self, coffee):
            if coffee >= 100:
                self.amnt_of_coffee = coffee
            else:
                raise NoCoffee

    class Water:
        # TODO docstring
        amnt_of_water = 0

        def get_water(self):
            return self.amnt_of_water

        def set_water(self, water):
            if water >= 100:
                self.amnt_of_water = water
            else:
                return False

    class NewIngredients(Beans, Water):

        def set_new_values_for_coffee_ingredients(self, amnt_coffee):
            # TODO doc string
            new_value_for_coffee = self.get_coffee()
            new_value_for_coffee -= amnt_coffee
            self.set_coffee(new_value_for_coffee)

        def set_new_values_for_water_ingredients(self, amnt_water):
            # TODO doc string
            new_value_for_water = self.get_water()
            new_value_for_water -= amnt_water
            self.set_water(new_value_for_water)
