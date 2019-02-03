from coffe_types.coffee import Espresso, Americano
from coffee_ingredient.ingredient import Ingredient
from Menu.menu import Menu
from Exception.custom_exception import Message


class CoffeeMaker(Menu, Ingredient.NewIngredients):

    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Order: ")

        if order == "1":
            e = Espresso()
            e.make_coffee(e.bean, e.water)
            self.set_new_values_for_coffee_ingredients(e.bean)
            self.set_new_values_for_water_ingredients(e.water)
            return e
        elif order == "2":
            a = Americano()
            a.make_coffee(a.bean, a.water)
            self.set_new_values_for_coffee_ingredients(a.bean)
            self.set_new_values_for_water_ingredients(a.water)
            return a
        elif order == "3":
            print(Message.canceled_order_message)
        else:
            print(Message.no_coffee_selected_message)


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
