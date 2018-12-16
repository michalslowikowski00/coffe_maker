import sqlite3


class CoffeeBeansTank:
    # TODO docstring
    amnt_of_coffee: int = 1000

    def get_coffee(self):
        return self.amnt_of_coffee

    def set_coffee(self, coffee):
        if coffee >= 100:
            self.amnt_of_coffee = coffee
        else:
            print("No coffee, please fill the coffee beans")
            return False


class WaterTank:
    # TODO docstring
    amnt_of_water: int = 1000

    def get_water(self):
        return self.amnt_of_water

    def set_water(self, water):
        if water >= 100:
            self.amnt_of_water = water
        else:
            print("No water, please fill the water tank")
            return False


def set_new_values_for_coffee_ingredients(self, amnt_of_coffee):
    # TODO doc string
    new_amnt_of_coffee = self.coffee.get_coffee()
    new_amnt_of_coffee -= amnt_of_coffee
    self.coffee.set_coffee(new_amnt_of_coffee)
    c.execute("UPDATE coffee SET value=(?) WHERE coffee='espresso'", new_amnt_of_coffee)



conn = sqlite3.connect("coffee.db")
c = conn.cursor()

# c.execute("""CREATE TABLE coffee (
#             coffee text,
#             value integer
#             )""")

# c.execute("INSERT INTO coffee VALUES ('espresso', 1000)")
# conn.commit()

c.execute("SELECT * FROM coffee WHERE coffee='espresso'")
# c.execute("UPDATE coffee SET value=1000 WHERE coffee='espresso'")

print(c.fetchone())

# conn.commit()
conn.close()


def update_coffee_in_database(new_value):

    new = CoffeeBeansTank()
    na = new.get_coffee()


    c.execute("UPDATE coffee SET value=(?) WHERE coffee='espresso'", new_value)
    conn.commit()
