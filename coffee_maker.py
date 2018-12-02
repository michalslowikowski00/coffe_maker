import coffee_beans_tank
import water_tank


class Coffee:
    # def __init__(self):
    customer_choice = input("Choice> ").lower()
    #TODO: menu for user

    # water = water_tank
    # coffee = coffee_beans_tank

    _espresso_water = 100
    _espresso_coffee_beans = 10
    _americano_water = 250
    _americano_coffee_beans = 5

    def make_coffee(self):
        water = water_tank
        coffee = coffee_beans_tank

        #TODO: try/catch

        if self.customer_choice == "espresso":
            print("Checking coffee...")
            if water.WaterTank.amount_water >= 100 and coffee_beans_tank.CoffeeBeansTank.amount_coffee_beans >= 10:
                pass
            else:
                if water.WaterTank.amount_water < 100:
                    print("Fill Water Tank")
                    return False
                elif coffee_beans_tank.CoffeeBeansTank.amount_coffee_beans < 5:
                    print("Fill Coffee Beans Tank")
                    return False
                else:
                    print("Fill Water Tank and Coffee Beans")
                    return False
            espresso = water.WaterTank.amount_water - self._espresso_water and \
                  coffee.CoffeeBeansTank.amount_coffee_beans - self._espresso_coffee_beans
            print("Preparing espresso, please wait a moment")
            return espresso

        elif self.customer_choice == "americano":
            americano = water.WaterTank.amount_water - self._americano_water and \
                        coffee.CoffeeBeansTank.amount_coffee_beans - self._americano_coffee_beans
            return americano
        else:
            return False
            # TODO: return except


if __name__ == "__main__":
    app = Coffee()
    app.make_coffee()
