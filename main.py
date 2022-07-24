MENU = {
    "espresso": {
        "ingredients": {
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


def calculate_money():
    """Takes input from customer in quarters, dime, nickles, pennies and converts them to dollars and returns it"""
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money_received = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return money_received


def is_resource_sufficient(choice_ingredients, left_ingredients):
    """Returns True if the resources are sufficient to make a drink and false when the resources are not sufficient"""
    for thing in resources:
        if choice_ingredients[thing] > left_ingredients[thing]:
            print(f"Sorry there is not enough {thing}. ")
            return False
        return True


def check_money(money, cost):
    """Returns True when the money is sufficient to buy a drink & false when the money is not sufficient"""
    if money >= cost:
        return True
    else:
        return False


profit = 0
machine_status = True

while machine_status:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        machine_status = False
        print("Machine is switched off")
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"], resources):
            coins = calculate_money()
            if check_money(coins, drink["cost"]):
                change = round(coins - drink["cost"], 2)
                print(f"Here is your {change} in change")
                print(f"Here is your {user_choice}")
                profit += drink["cost"]
                # make_drink(drink["ingredients"], coins)
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
            else:
                print("Sorry that's not enough money. Money refunded.")