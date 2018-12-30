
class Ingredients:

    class CoffeeBeansTank:
        # TODO docstring
        amnt_of_coffee: int = 1000

        def get_coffee(self):
            return self.amnt_of_coffee

        def set_coffee(self, coffee):
            if coffee >= 100:
                self.amnt_of_coffee = coffee
            else:
                print("No coffee, please fill the coffee beans")
                return False

    class WaterTank:
        # TODO docstring
        amnt_of_water = 1000

        def get_water(self):
            return self.amnt_of_water

        def set_water(self, water):
            if water >= 100:
                self.amnt_of_water = water
            else:
                print("No water, please fill the water tank")
                return False

    class NewIngredients(CoffeeBeansTank, WaterTank):

        def set_new_values_for_coffee_ingredients(self, amnt_coffee):
            # TODO doc string

            new_value_for_coffee = self.get_coffee()
            new_value_for_coffee -= amnt_coffee
            self.set_coffee(new_value_for_coffee)


            #
            # new_coffee_ingr = self.get_coffee()
            # new_coffee_ingr -= amnt_coffee
            # self.set_coffee(amnt_coffee)


            # coffee_ingr -= new_amnt_coffee
            # CoffeeBeansTank.set_coffee(coffee_ingr)
            # # self.coffee.set_coffee(new_amnt_of_coffee)
            # return coffee_ingr
