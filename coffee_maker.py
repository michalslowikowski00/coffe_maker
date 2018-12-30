from coffee import Espresso, Americano, Coffee
from ingredients import Ingredients
from menu import Menu
from messages import Messages


class MakeCoffee(Espresso, Americano, Menu, Ingredients.NewIngredients, Coffee):

    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Order > ").lower()

        if order == "1":
            if not self.espresso():
                return False
            print(Messages.checking_coffee)
            print(Messages.preparing_espresso)
            print(Messages.coffee_is_ready)
            # print(self.set_new_values_for_coffee_ingredients(self.coffee_for_espresso))

            #TODO: set new amount of coffee

        elif order == "2":
            if not self.americano():
                return False
            print(Messages.checking_coffee)
            print(Messages.preparing_americano)
            print(Messages.coffee_is_ready)
            # TODO: set new amount of coffee

        elif order == "3":
            print(Messages.canceled_order)
        else:
            print(Messages.no_coffee_selected)


if __name__ == "__main__":
    app = MakeCoffee()
    app.make_coffee()
