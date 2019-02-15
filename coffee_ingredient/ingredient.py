from Exception.custom_exception import NoCoffee


class Ingredient:

    def isBeanContainerEmpty(self, coffee_ingr_needed):
        b = BeanContainer()

        if b.amount_of_bean < coffee_ingr_needed:
            raise NoCoffee
        return



        # return
        # yield

    @property
    def isWaterContainerEmpty(self):
        return
        # yield


class BeanContainer(Ingredient):
    def __init__(self, amount_of_bean=0):
        self.amount_of_bean = amount_of_bean


class WaterContainer(Ingredient):
    def __init__(self, amount_of_water=1000):
        self.amount_of_water = amount_of_water


if __name__ == "__main__":
    pass


