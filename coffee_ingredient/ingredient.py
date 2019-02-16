from exception.custom_exception import NoCoffee, NoWater


class Ingredient:
    @property
    def bean(self):
        b = BeanContainer()
        return b.amount_of_bean

    @property
    def water(self):
        w = WaterContainer()
        return w.amount_of_water


class BeanContainer(Ingredient):
    def __init__(self, amount_of_bean=1000):
        self.amount_of_bean = amount_of_bean

    def get_coffee(self):
        return self.amount_of_bean

    def set_coffee(self, coffee):
        if coffee >= 100:
            self.amount_of_bean = coffee
        else:
            raise NoCoffee(
                "Amount of Coffee in class Beans: {0}".format(self.amount_of_bean)
            )

    def set_new_values_for_coffee_ingredients(self, amount_of_beans):
        # TODO doc string
        new_value_for_coffee = self.get_coffee()
        new_value_for_coffee -= amount_of_beans
        self.set_coffee(new_value_for_coffee)


class WaterContainer(Ingredient):
    def __init__(self, amount_of_water=1000):
        self.amount_of_water = amount_of_water

    def get_water(self):
        return self.amount_of_water

    def set_water(self, water):
        if water >= 100:
            self.amount_of_water = water
        else:
            raise NoWater(
                "Amount of Water in class Water: {0}".format(self.amount_of_water)
            )

    def set_new_values_for_water_ingredients(self, amount_of_water):
        # TODO doc string
        new_value_for_water = self.get_water()
        new_value_for_water -= amount_of_water
        self.set_water(new_value_for_water)
