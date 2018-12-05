from pprint import pprint
import coffe_ingredients


class CoffeeMaker:
    coffee = coffe_ingredients.CoffeeBeansTank()
    water = coffe_ingredients.WaterTank()
    get_coffee_ingredients = coffe_ingredients.CoffeeBeansTank()

    # TODO: fix this values

    amount_of_water_for_espresso = 100
    amount_of_coffee_for_espresso = 15

    amount_of_water_for_americano = 250
    amount_of_coffee_for_americano = 10

    def display_coffee_menu(self):
        """Display available coffee for customer"""
        espresso = "1. Espresso"
        americano = "2. Americano"
        print(espresso + "\n" + americano)

    def make_coffee(self):
        """Make coffee based on customer order"""

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
            pprint(self.get_coffee_ingredients.getCoffee())

            #TODO: change var names
            self.new_amount = self.get_coffee_ingredients.getCoffee()
            new_amount = self.new_amount - self.amount_of_coffee_for_espresso

            self.get_coffee_ingredients.setCoffee(new_amount)
            pprint(self.get_coffee_ingredients.getCoffee())
            #TODO: add new water amount var
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
