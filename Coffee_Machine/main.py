MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_in_till = round(0.00, 2)
total_money = round(0.00, 2)

is_on = True


def resources_available(coffee_type):
    if coffee_type == 'espresso':
        if ((MENU['espresso']["ingredients"]["milk"]) <= (resources["milk"])) & (
                (MENU['espresso']['ingredients']["water"]) <= (resources['water'])) & (
                (MENU['espresso']["ingredients"]["coffee"]) <= (resources['coffee'])):
            return True
        else:
            return False

    elif coffee_type == 'latte':
        if ((MENU['latte']["ingredients"]["milk"]) <= (resources["milk"])) & (
                (MENU['latte']['ingredients']["water"]) <= (resources['water'])) & (
                (MENU['latte']["ingredients"]["coffee"]) <= (resources['coffee'])):
            return True
        else:
            return False

    elif coffee_type == 'cappuccino':
        if ((MENU['cappuccino']["ingredients"]["milk"]) <= (resources["milk"])) & (
                (MENU['cappuccino']['ingredients']["water"]) <= (resources['water'])) & (
                (MENU['cappuccino']["ingredients"]["coffee"]) <= (resources['coffee'])):
            return True
        else:
            return False


def money_available(coffee_type, quarters, dimes, nickels, pennies):
    global total_money

    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if coffee_type == 'espresso':
        if (MENU['espresso']["cost"]) <= total_money:
            return True
    elif coffee_type == 'latte':
        if (MENU['latte']["cost"]) <= total_money:
            return True
    elif coffee_type == 'cappuccino':
        if (MENU['cappuccino']["cost"]) <= total_money:
            return True
    else:
        print("Sorry that's not enough money. Money refunded")


def coffee_machine():
    global money_in_till

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == 'off':
        exit()
    elif user_input == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money in the till: {round(money_in_till, 2)}")
        coffee_machine()

    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        if resources_available(user_input):

            print(f"The price for {user_input} is ${(MENU[user_input]['cost'])}.")
            print("Please insert coins.")

            quarters_input = float(input("How many quarters?: "))
            dimes_input = float(input("How many dimes?: "))
            nickel_input = float(input("How many nickles?: "))
            pennies_input = float(input("How many pennies?: "))

            if money_available(user_input, quarters_input, dimes_input, nickel_input, pennies_input):
                money_in_till = money_in_till + (MENU[user_input]['cost'])
                resources["water"] = resources["water"] - (MENU[user_input]['ingredients']['water'])
                resources["milk"] = resources["milk"] - (MENU[user_input]['ingredients']['milk'])
                resources["coffee"] = resources["coffee"] - (MENU[user_input]['ingredients']['coffee'])

                change = round(total_money - (MENU[user_input]['cost']), 2)

                print(f"Here is your ${change} in change.")
                print(f"Here is your {user_input} ready, Enjoy!")
                coffee_machine()
            else:
                print("Sorry, that's not enough money. Money Refunded.")
                coffee_machine()

        else:
            print("Sorry, we do not have enough resources.")

    else:
        print("Please give the correct input. Thanks!")
        coffee_machine()


while is_on:
    coffee_machine()
