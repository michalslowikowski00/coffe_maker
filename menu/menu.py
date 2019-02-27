
class Menu:

    # menu = {1: "Espresso",
    #         2: "Americano",
    #         3: "Cancel"
    #         }

    @staticmethod
    def display_coffee_menu():
        """Display available menu for customer"""
        espresso = "1. Espresso"
        americano = "2. Americano"
        cancel = "3. Cancel"
        print(espresso + "\n" + americano + "\n" + cancel)
        # print(" 1. " + Menu.menu[1] + "\n",
        #       "2. " + Menu.menu[2] + "\n",
        #       "3. " + Menu.menu[3] + "\n")

