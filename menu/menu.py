from enum import Enum


class Menu(Enum):

    ESPRESSO = 1
    AMERICANO = 2
    CANCEL = 3

    def display_coffee_menu(self):
        """Display available menu for customer"""
        espresso = "1. Espresso"
        americano = "2. Americano"
        cancel = "3. Cancel"
        print(espresso + "\n" + americano + "\n" + cancel)
