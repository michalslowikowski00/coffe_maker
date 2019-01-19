from Coffe_Types.coffee import Espresso, Americano
from Coffee_Ingredient.ingredient import Ingredient
from Menu.menu import Menu
from Messeges.messages import Messages


class CoffeeMaker(Menu, Ingredient.NewIngredients, Ingredient.Coffee, Ingredient.Beans):

    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Order > ").lower()

        # TODO: add switch instead of if / else
        if order == "1":
            espresso = Espresso()
            espresso.make_coffee(espresso.bean, espresso.water)
            print(Messages.checking_coffee)
            print(Messages.preparing_espresso)
            print(Messages.coffee_is_ready)
            self.set_new_values_for_coffee_ingredients(Ingredient.Coffee.coffee_for_espresso)
            self.set_new_values_for_water_ingredients(Ingredient.Coffee.water_for_espresso)
            print(Ingredient.Beans.get_coffee(self))
            print(Ingredient.Water.get_water(self))
            return espresso
            # TODO set new value to data base

        elif order == "2":
            americano = Americano()
            print(Messages.checking_coffee)
            print(Messages.preparing_americano)
            print(Messages.coffee_is_ready)
            self.set_new_values_for_coffee_ingredients(Ingredient.Coffee.coffee_for_americano)
            self.set_new_values_for_water_ingredients(Ingredient.Coffee.water_for_americano)
            return americano
            # TODO set new value to data base

        elif order == "3":
            print(Messages.canceled_order)
        else:
            print(Messages.no_coffee_selected)


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
