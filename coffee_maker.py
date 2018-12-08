import coffe_ingredients


class CoffeeMaker:
    # TODO docstring
    water = coffe_ingredients.WaterTank()
    coffee = coffe_ingredients.CoffeeBeansTank()

    water_for_espresso = 100
    coffee_for_espresso = 15

    water_for_americano = 250
    coffee_for_americano = 10


    @staticmethod
    def display_coffee_menu():
        """Display available coffee for customer"""
        espresso = "1. Espresso"
        americano = "2. Americano"
        cancel = "3. Cancel"
        print(espresso + "\n" + americano + "\n" + cancel)

    # TODO: add button for preparing coffee
    # TODO: add data base for saving amount of water and coffee

    def espresso(self):
        # TODO docstring

        if self.water.amount_of_water < self.water_for_espresso:
            print("No water, Fill the water tank")
            return False
        elif self.coffee.amount_of_coffee < self.coffee_for_espresso:
            print("No coffee beans, fill the coffee tank")
            return False
        return True

    def americano(self):
        # TODO docstring
        if self.water.amount_of_water < self.water_for_americano:
            print("No water, Fill the water tank")
            return False
        elif self.coffee.amount_of_coffee < self.coffee_for_americano:
            print("No coffee beans, fill the coffee tank")
            return False
        return True

    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Choice > ").lower()

        # print("Something went wrong, please try again")

        if order == "1":
            print("Checking coffee...")
            try:
                self.espresso()
            except Exception as e:
                print(e)
            print("Preparing Espresso, please wait a moment")
            print("Coffee is ready, take your drink")
            print(self.coffee.get_coffee())
            self.set_new_values_for_coffee_ingredients(self.coffee_for_espresso)

        elif order == "2":
            print("Checking coffee...")
            print("Coffee in tank: {0} grams".format(self.coffee.get_coffee()))
            try:
                self.americano()
            except RuntimeError:
                print("No coffee selected")
            print("Preparing Americano, please wait a moment")
            print("Coffee is ready, take your drink")
            self.set_new_values_for_coffee_ingredients(self.coffee_for_americano)
            # print("Coffee left in tank after this coffee: {0} grams".format(self.coffee.get_coffee()))
        elif order == "3":
            print("Order was canceled")
        else:
            print("No coffee selected. Please select coffee.")

    def set_new_values_for_coffee_ingredients(self, amnt_of_coffee):
        # TODO docstring
        new_amount_of_coffee = self.coffee.get_coffee()
        new_amount_of_coffee -= amnt_of_coffee
        self.coffee.set_coffee(new_amount_of_coffee)
        print(self.coffee.get_coffee())


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
