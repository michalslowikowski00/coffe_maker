from Coffe_Types.coffee import Espresso, Americano
from Coffee_Ingredient.ingredient import Ingredient
from Menu.menu import Menu
from Messeges.messages import Messages


class CoffeeMaker(Menu, Ingredient.NewIngredients, Ingredient.Coffee, Ingredient.Beans):

    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Order: ")

        if order == "1":
            espresso = Espresso()
            espresso.make_coffee(espresso.bean, espresso.water)
            self.set_new_values_for_coffee_ingredients(Ingredient.Coffee.coffee_for_espresso)
            self.set_new_values_for_water_ingredients(Ingredient.Coffee.water_for_espresso)
            return espresso

        elif order == "2":
            americano = Americano()
            americano.make_coffee(americano.bean, americano.water)
            self.set_new_values_for_coffee_ingredients(Ingredient.Coffee.coffee_for_americano)
            self.set_new_values_for_water_ingredients(Ingredient.Coffee.water_for_americano)
            return americano

        elif order == "3":
            print(Messages.canceled_order)

        else:
            print(Messages.no_coffee_selected)


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
