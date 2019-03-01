from Exception.custom_exception import Message
from Menu.menu import Menu
from coffee.coffee import Espresso, Americano
from ingredient.ingredient import BeanContainer, WaterContainer


class CoffeeMaker:
    def brew_coffee(self):
        """Make coffee based on customer order"""
        menu = Menu()
        menu.display_coffee_menu()
        order = input("Order: ")

        bean_container = BeanContainer()
        water_container = WaterContainer()

        if order == "1":
            espresso = Espresso()
            espresso.make_coffee(espresso.bean, espresso.water)
            bean_container.set_new_values_for_coffee_ingredients(espresso.bean)
            water_container.set_new_values_for_water_ingredients(espresso.water)
            return espresso
        elif order == "2":
            americano = Americano()
            print(water_container.water)
            americano.make_coffee(americano.bean, americano.water)
            bean_container.set_new_values_for_coffee_ingredients(americano.bean)
            water_container.set_new_values_for_water_ingredients(americano.water)
            return americano
        elif order == "3":
            print(Message.canceled_order_message)
        else:
            print(Message.no_coffee_selected_message)


if __name__ == "__main__":
    app = CoffeeMaker()
    while True:
        app.brew_coffee()
