from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
while is_on:
    cash = MoneyMachine()
    maker = CoffeeMaker()
    the_menu = Menu()
    console_input = input(f"What would you like? {the_menu.get_items()}\n").lower()

    if console_input == "report":
        maker.report()

    elif console_input == "off":
        is_on = False

    elif console_input in the_menu.get_items():
        drink = (Menu.find_drink(the_menu, console_input))
        if maker.is_resource_sufficient(drink):
            price = drink.cost
            print(f"Your {console_input} is ${price}")
            if cash.make_payment(price):
                maker.make_coffee(drink)
