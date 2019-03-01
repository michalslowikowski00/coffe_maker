from exception.custom_exception import Message
from menu.menu import Menu, Order
from coffee.coffee import Espresso, Americano
from ingredient.ingredient import BeanContainer, WaterContainer


class CoffeeMaker:

    def brew_coffee(self):
        """Make coffee based on customer order"""
        menu = Menu()
        menu.display_menu()
        coffee = int(input("Select coffee: "))

        bean_container = BeanContainer()
        water_container = WaterContainer()

        if coffee == Order.ESPRESSO.value:
            espresso = Espresso()
            espresso.make_coffee(espresso.bean, espresso.water)
            # bean_container.set_new_values_for_coffee_ingredients(espresso.bean)
            # water_container.set_new_values_for_water_ingredients(espresso.water)
            return espresso
        elif coffee == Order.AMERICANO.value:
            americano = Americano()
            americano.make_coffee(americano.bean, americano.water)
            # bean_container.set_new_values_for_coffee_ingredients(americano.bean)
            # water_container.set_new_values_for_water_ingredients(americano.water)
            return americano
        elif coffee == Order.CANCEL.value:
            print(Message.canceled_order_message)
        else:
            print(Message.no_coffee_selected_message)


if __name__ == "__main__":
    app = CoffeeMaker()
    while True:
        app.brew_coffee()
