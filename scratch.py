# import coffe_ingredients
# from messages import Messages
#
#
# class CoffeeMaker:
#     # TODO docstring
#     water = coffe_ingredients.WaterTank()
#     coffee = coffe_ingredients.CoffeeBeansTank()
#     messages = Messages
#
#     # coffee_ingr = {"espresso_water": 100,
#     #               "americano_water": 250,
#     #               "coffee_espresso": 15,
#     #               "coffee_for_americano": 10}
#
#     water_for_espresso = 100
#     coffee_for_espresso = 15
#     water_for_americano = 250
#     coffee_for_americano = 10
#
#     @staticmethod
#     def display_coffee_menu():
#         """Display available menu for customer"""
#         espresso = "1. Espresso"
#         americano = "2. Americano"
#         cancel = "3. Cancel"
#         print(espresso + "\n" + americano + "\n" + cancel)
#         return
#
#     # TODO: add button for preparing coffee
#     # TODO: add data base for saving amount of water and coffee
#
#     def americano(self):
#         # TODO doc string
#         if self.water.amnt_of_water < self.water_for_americano:
#             print(Messages.no_water)
#             return False
#         elif self.coffee.amnt_of_coffee < self.coffee_for_americano:
#             print(Messages.no_coffee)
#             return False
#         return True
#
#     def espresso(self):
#         # TODO docstring
#         if self.water.amnt_of_water < self.water_for_espresso:
#             print(Messages.no_water)
#             return False
#         elif self.coffee.amnt_of_coffee < self.coffee_for_espresso:
#             print(Messages.no_coffee)
#             return False
#         return True
#
#     def make_coffee(self):
#         """Make coffee based on customer order"""
#         self.display_coffee_menu()
#         order = input("Choice > ").lower()
#
#         if order == "1":
#             self.espresso()
#             self.set_new_values_for_coffee_ingredients(self.coffee_for_espresso)
#             self.set_new_values_for_water_ingredients(self.water_for_espresso)
#             print(Messages.checking_coffee)
#             print(Messages.preparing_espresso)
#             print(Messages.coffee_is_ready)
#         elif order == "2":
#             self.americano()
#             self.set_new_values_for_coffee_ingredients(self.coffee_for_americano)
#             self.set_new_values_for_water_ingredients(self.water_for_americano)
#             print(Messages.checking_coffee)
#             print(Messages.preparing_americano)
#             print(Messages.coffee_is_ready)
#         elif order == "3":
#             print(Messages.canceled_order)
#         else:
#             print(Messages.no_coffee_selected)
#         return
#
#     def set_new_values_for_coffee_ingredients(self, amnt_of_coffee):
#         # TODO doc string
#         new_amnt_of_coffee = self.coffee.get_coffee()
#         new_amnt_of_coffee -= amnt_of_coffee
#         self.coffee.set_coffee(new_amnt_of_coffee)
#
#     def set_new_values_for_water_ingredients(self, amnt_of_water):
#         # TODO doc string
#         new_amnt_of_water = self.water.get_water()
#         new_amnt_of_water -= amnt_of_water
#         self.water.set_water(new_amnt_of_water)
#         return
#
#
# if __name__ == "__main__":
#     app = CoffeeMaker()
#     app.make_coffee()
