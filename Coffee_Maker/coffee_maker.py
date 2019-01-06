from Coffe_Types.coffee import Espresso, Americano
from Coffee_Ingredients.ingredients import Ingredients
from Menu.menu import Menu
from Messeges.messages import Messages


class MakeCoffee(Menu, Ingredients.NewIngredients, Ingredients.Coffee, Ingredients.Beans):

    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Order > ").lower()

        # TODO: add switch instead of if / else
        if order == "1":

            espresso = Espresso(Espresso.bean_espresso, Espresso.water_espresso)
            print(Messages.checking_coffee)
            print(Messages.preparing_espresso)
            print(Messages.coffee_is_ready)
            self.set_new_values_for_coffee_ingredients(Ingredients.Coffee.coffee_for_espresso)
            self.set_new_values_for_water_ingredients(Ingredients.Coffee.water_for_espresso)
            return espresso
            # TODO set new value to data base

        elif order == "2":
            americano = Americano(Americano.bean_americano, Americano.water_americano)
            print(Messages.checking_coffee)
            print(Messages.preparing_americano)
            print(Messages.coffee_is_ready)
            self.set_new_values_for_coffee_ingredients(Ingredients.Coffee.coffee_for_americano)
            self.set_new_values_for_water_ingredients(Ingredients.Coffee.water_for_americano)
            return americano
            # TODO set new value to data base

        elif order == "3":
            print(Messages.canceled_order)
        else:
            print(Messages.no_coffee_selected)


if __name__ == "__main__":
    app = MakeCoffee()
    app.make_coffee()
