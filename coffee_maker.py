import coffe_ingredients
from messages import Messages


class CoffeeMaker:
    # TODO docstring
    water = coffe_ingredients.WaterTank()
    coffee = coffe_ingredients.CoffeeBeansTank()
    messages = Messages

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
            print(Messages.no_water)
            return False
        elif self.coffee.amount_of_coffee < self.coffee_for_espresso:
            print(Messages.no_coffee)
            return False
        return True

    def americano(self):
        # TODO docstring
        if self.water.amount_of_water < self.water_for_americano:
            print(Messages.no_water)
            return False
        elif self.coffee.amount_of_coffee < self.coffee_for_americano:
            print(Messages.no_coffee)
            return False
        return True

    def make_coffee(self):
        """Make coffee based on customer order"""
        self.display_coffee_menu()
        order = input("Choice > ").lower()

        if order == "1":
            print(Messages.checking_coffee)
            self.espresso()
            print(Messages.preparing_espresso)
            print(Messages.coffee_is_ready)
            self.set_new_values_for_coffee_ingredients(self.coffee_for_espresso)

        elif order == "2":
            print(Messages.checking_coffee)
            print(Messages.left_coffee_in_tank.format(self.coffee.get_coffee()))
            self.americano()
            print(Messages.preparing_americano)
            print(Messages.coffee_is_ready)
            self.set_new_values_for_coffee_ingredients(self.coffee_for_americano)
        elif order == "3":
            print(Messages.canceled_order)
        else:
            print(Messages.no_coffee_selected)

    def set_new_values_for_coffee_ingredients(self, amnt_of_coffee):
        # TODO docstring
        new_amount_of_coffee = self.coffee.get_coffee()
        new_amount_of_coffee -= amnt_of_coffee
        self.coffee.set_coffee(new_amount_of_coffee)


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
