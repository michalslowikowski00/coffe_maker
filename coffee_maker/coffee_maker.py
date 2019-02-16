from coffe_types.coffee import Espresso, Americano
from coffee_ingredient.ingredient import Ingredient, BeanContainer, WaterContainer
from menu.menu import Menu
from exception.custom_exception import Message


class CoffeeMaker(Menu, Ingredient):
    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Order: ")
        e = Espresso()
        a = Americano()
        b = BeanContainer()
        w = WaterContainer()

        if order == "1":
            e.make_coffee(e.bean, e.water)
            b.set_new_values_for_coffee_ingredients(e.bean)
            w.set_new_values_for_water_ingredients(e.water)
            print(b.amount_of_bean)
            print(w.amount_of_water)
            return e
        elif order == "2":
            a.make_coffee(a.bean, a.water)
            b.set_new_values_for_coffee_ingredients(a.bean)
            w.set_new_values_for_water_ingredients(a.water)
            return a
        elif order == "3":
            print(Message.canceled_order_message)
        else:
            print(Message.no_coffee_selected_message)


if __name__ == "__main__":
    app = CoffeeMaker()
    # while True:
    app.make_coffee()
