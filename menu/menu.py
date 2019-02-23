class Menu:

    @staticmethod
    def display_coffee_menu():
        """Display available menu for customer"""
        espresso = "1. Espresso"
        americano = "2. Americano"
        cancel = "3. Cancel"
        print(espresso + "\n" + americano + "\n" + cancel)
