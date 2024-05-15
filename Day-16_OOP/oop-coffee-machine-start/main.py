from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")

    if choice == 'report':
        coffee_machine.report()
        money_machine.report()

    elif choice == 'end':
        is_on = False
        exit()
    elif (choice == 'latte') or (choice == 'espresso') or (choice == 'cappuccino'):
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    else:
        print("Please give a right input, Thanks!")