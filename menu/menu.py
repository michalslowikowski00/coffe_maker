from enum import Enum


class Order(Enum):

    ESPRESSO = 1
    AMERICANO = 2
    CANCEL = 3


class Menu:

    espresso = "1. Espresso"
    americano = "2. Americano"
    cancel = "3. Cancel"

    def display_menu(self):
        """Display available menu for customer"""
        print(self.espresso + "\n" + self.americano + "\n" + self.cancel)
