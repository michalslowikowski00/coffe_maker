from Exception.custom_exception import NoCoffee


class Ingredient:

    def isBeanContainerEmpty(self, bean):
        bc = BeanContainer()

        if bc.amount_of_bean < bean:
            raise NoCoffee
        return bc

    @property
    def isWaterContainerEmpty(self):
        return


class BeanContainer(Ingredient):
    def __init__(self, amount_of_bean=1000):
        self.amount_of_bean = amount_of_bean


class WaterContainer(Ingredient):
    def __init__(self, amount_of_water=1000):
        self.amount_of_water = amount_of_water


if __name__ == "__main__":
    pass
