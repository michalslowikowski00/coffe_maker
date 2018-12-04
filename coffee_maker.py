# import coffee_beans_tank
# import water_tank
from logging import log, info, debug
from pprint import pprint

import coffe_ingredients
# from msvcrt import getch


class CoffeeMaker:  # TODO: dzidziczenie
    water = coffe_ingredients.WaterTank()
    coffee = coffe_ingredients.CoffeeBeansTank()

    amount_of_water_for_espresso = 100
    amount_of_coffee_for_espresso = 15

    amount_of_water_for_americano = 250
    amount_of_coffee_for_americano = 10

    def display_coffee_menu(self):
        """Display available coffee for customer"""
        espresso = "1. Espresso"
        americano = "2. Americano"
        print(espresso + "\n" + americano)

    # def press_button(self):
    #
    #     while True:
    #         key = ord(getch())
    #         if key == 27:  # ESC
    #             break
    #         elif key == 13:  # Enter
    #             select()
    #         elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
    #             key = ord(getch())
    #             if key == 80:  # Down arrow
    #                 moveDown()
    #             elif key == 72:  # Up arrow
    #                 moveUp()

    def make_coffee(self):
        """Make coffee based on customer order"""

        get_coffee = coffe_ingredients.CoffeeBeansTank()
        self.display_coffee_menu()
        order = input("Choice > ").lower()

        if order == "espresso":
            pprint("Checking coffee...")
            if self.water.amount_of_water < 100:
                pprint("No water, Fill the watertank")
                return False
            elif self.coffee.amount_of_coffee < 15:
                pprint("No coffee beans, fill the coffeetank")
                return False
            pprint("Preparing Espresso, please wait a moment")
            pprint("Coffee is ready, take your drink")
            pprint(get_coffee.getCoffee())

            self.new_amount = get_coffee.getCoffee()
            self.new_amount = self.new_amount - self.amount_of_coffee_for_espresso
            get_coffee.setCoffee(self.new_amount)
            pprint(get_coffee.getCoffee())
            return True

        elif order == "americano":
            if self.water.amount_of_water < 250:
                pprint("Fill the Water Tank")
                return False
            elif self.coffee.amount_of_coffee < 10:
                pprint("Fill the Beans Tank")
                return False
            pprint("Preparing Americano, please wait a moment")
            pprint("Coffee is ready, take your drink")
            return True
        else:
            pprint("No coffee selected.\nPlease select coffee.")
            self.display_coffee_menu()


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
