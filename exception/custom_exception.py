
class NoBeanError(BaseException):
    """Raised when the value of amnt_of_bean in Ingredient.Beans is too small"""

    no_coffee_message = "No coffee beans, fill the coffee tank"


class NoWaterError(BaseException):
    """Raised when the value of amnt_of_water in Ingredient.Water is less then 100"""

    no_water_message = "No water, fill the water tank"


class Message:
    """ Module with messages that are used in modules coffee.py. """

    checking_coffee_message = "Checking coffee..."
    preparing_coffee_message = "Preparing coffee, please wait a moment"
    coffee_is_ready_message = "Coffee is ready, take your drink"
    canceled_order_message = "Order was canceled"
    no_coffee_selected_message = "No coffee selected. Please select coffee."
