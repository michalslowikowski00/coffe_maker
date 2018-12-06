from pprint import pprint
import coffe_ingredients


class CoffeeMaker:
    water = coffe_ingredients.WaterTank()
    coffee = coffe_ingredients.CoffeeBeansTank()

    water_for_espresso = 100
    coffee_for_espresso = 15

    water_for_americano = 250
    coffee_for_americano = 10


    @staticmethod
    def display_coffee_menu():
        """Display available coffee for customer"""
        try:
            espresso = "1. Espresso"
            americano = "2. Americano"
            print(espresso + "\n" + americano)
        except RuntimeError:
            print("Menu was not displayed")


    # TODO: add button for preparing coffee

    def espresso(self):
        if self.water.amount_of_water < self.water_for_espresso:
            pprint("No water, Fill the watertank")
            return False
        elif self.coffee.amount_of_coffee < self.coffee_for_espresso:
            pprint("No coffee beans, fill the coffeetank")
            return False
        return True

    def americano(self):
        if self.water.amount_of_water < self.water_for_americano:
            pprint("No water, Fill the watertank")
            return False
        elif self.coffee.amount_of_coffee < self.coffee_for_americano:
            pprint("No coffee beans, fill the coffeetank")
            return False
        return True

    def make_coffee(self):
        """Make coffee based on customer order"""
        try:
            self.display_coffee_menu()
            order = input("Choice > ").lower()
        except RuntimeError:
            pprint("Something went wrong, please try again")

        if order == "espresso":
            pprint("Checking coffee...")
            try:
                self.espresso()
            except RuntimeError:
                pprint("No coffee selected")
            pprint("Preparing Espresso, please wait a moment")
            pprint("Coffee is ready, take your drink")
            pprint(self.coffee.get_coffee())
            self.set_new_values_for_coffee_ingredients()

        elif order == "americano":
            pprint("Checking coffee...")
            pprint("Coffee in tank: {0} grams".format(self.coffee.get_coffee()))
            try:
                self.americano()
            except RuntimeError:
                pprint("No coffee selected")
            pprint("Preparing Americano, please wait a moment")
            pprint("Coffee is ready, take your drink")
            self.set_new_values_for_coffee_ingredients()
            pprint("Coffee left in tank after this coffee: {0} grams".format(self.coffee.get_coffee()))
        else:
            pprint("No coffee selected. Please select coffee.")
            print(" ")
            self.make_coffee()

    def set_new_values_for_coffee_ingredients(self):
        new_amount_of_coffee = self.coffee.get_coffee()
        new_amount_of_coffee = new_amount_of_coffee - self.coffee_for_espresso
        self.coffee.set_coffee(new_amount_of_coffee)
        pprint(self.coffee.get_coffee())


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
