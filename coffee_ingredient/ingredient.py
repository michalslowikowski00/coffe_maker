from coffe_types.coffee import Coffee
from Exception.custom_exception import NoCoffee



class Ingredient:

    def isBeanContainerEmpty(self):
        b = BeanContainer()
        c = Coffee()

        if b.amount_of_bean < c.bean:
            raise NoCoffee
        return Ingredient

    @property
    def isWaterContainerEmpty(self):
        return
        # yield

    def pr(self):
        print()


class BeanContainer(Ingredient):
    def __init__(self, amount_of_bean=1000):
        self.amount_of_bean = amount_of_bean


class WaterContainer(Ingredient):
    def __init__(self, amount_of_water=1000):
        self.amount_of_water = amount_of_water


if __name__ == "__main__":
    pass
