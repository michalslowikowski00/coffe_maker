# import coffee_beans_tank
# import water_tank
import coffe_ingredients
from msvcrt import getch


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

    def press_button(self):

        while True:
            key = ord(getch())
            if key == 27:  # ESC
                break
            elif key == 13:  # Enter
                select()
            elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
                key = ord(getch())
                if key == 80:  # Down arrow
                    moveDown()
                elif key == 72:  # Up arrow
                    moveUp()

    def make_coffee(self):
        """Make coffee based on customer order"""

        self.display_coffee_menu()
        order = input("Choice> ").lower()

        if order == "espresso":
            print("Checking coffee...")
            if self.water.amount_of_water < 100:
                print("No water, Fill the watertank")
                return False
            elif self.coffee.amount_of_coffee < 15:
                print("No coffee beans, fill the coffeetank")
                return False
            print("Preparing Espresso, please wait a moment")
            print("Coffee is ready, take your drink")
            return True

        elif order == "americano":
            if self.water.amount_of_water < 250:
                print("Fill the Water Tank")
                return False
            elif self.coffee.amount_of_coffee < 10:
                print("Fill the Beans Tank")
                return False
            print("Preparing Americano, please wait a moment")
            print("Coffee is ready, take your drink")
            return True
        else:
            print("No coffee selected.\nPlease select coffee.")
            self.display_coffee_menu()


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
