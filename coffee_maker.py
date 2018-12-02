# import coffee_beans_tank
# import water_tank
import coffe_ingredients


class CoffeeMaker(coffe_ingredients): #TODO: dzidziczenie
    # def __init__(self):
    #     self.customer_choice = input("Choice> ").lower()

    def coffee_menu(self):
        """Displays available coffee for customer"""
        espresso = "1. espresso"
        americano = "2. americano"
        print(espresso + "\n" + americano)

    # customer_choice = input("Choice> ").lower()

    #TODO: fix the method
    # def choice(self):
    #
    #     return customer_choice

    #TODO: menu for user
    # water = water_tank
    # coffee = coffee_beans_tank

    _espresso_water = 100
    _espresso_coffee_beans = 10
    _americano_water = 250
    _americano_coffee_beans = 5

    def make_coffee(self):
        # rename to order?
        """Make coffee based on customer order"""
        water = coffe_ingredients.WaterTank
        coffee = coffe_ingredients.CoffeeBeansTank

        # self.coffee_menu()
        # self.choice()

        #TODO: try/catch
        #TODO: make_coffee jako metoda z argumentem rodzaj kawy
        #TODO: CoffeeIngredients insted of WaterTank & CoffeeBeansTank

        self.coffee_menu()
        self.customer_choice = input("Choice> ").lower()

        if self.customer_choice == "espresso":
            print("Checking coffee...")
            if water.amount_water >= 100 and coffee.amount_coffee_beans >= 10:
                pass
            else:
                if water.amount_water < 100:
                    print("Fill Water Tank")
                    return False
                elif coffee.amount_coffee_beans < 5:
                    print("Fill Coffee Beans Tank")
                    return False
                else:
                    print("Fill Water Tank and Coffee Beans")
                    return False
            espresso = water.amount_water - self._espresso_water and \
                  coffee.amount_coffee_beans - self._espresso_coffee_beans
            print("Preparing espresso, please wait a moment")
            print("Coffee is ready, take your drink")
            return espresso

        elif self.customer_choice == "americano":
            americano = water.amount_water - self._americano_water and \
                        coffee.amount_coffee_beans - self._americano_coffee_beans
            return americano
        else:
            print("Selected item is not in menu")
            self.coffee_menu()
            # TODO: return except


if __name__ == "__main__":
    app = CoffeeMaker()
    app.make_coffee()
