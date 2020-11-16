MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money":0,
}
def check_products(Type):
    req_water = MENU[Type]["ingredients"]["water"]
    req_milk = MENU[Type]["ingredients"]["milk"]
    req_coffee = MENU[Type]["ingredients"]["coffee"]
    req_money = MENU[Type]["cost"]
    if resources["water"] < req_water:
        print("Sorry there's not enough Water")
        return False
    elif resources["milk"] < req_milk:
        print("Sorry there's not enough Milk")
        return False
    elif resources["coffee"] < req_coffee:
        print("Sorry there's not enough Coffee")
        return False
    else:
        resources["water"] -= req_water
        resources["milk"] -= req_milk
        resources["coffee"] -= req_coffee
        resources["money"] += req_money
        return True

def get_and_calc_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01


def requirements(dollar, Type):
    if dollar < MENU[Type]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    else:
        if check_products(Type):
            if dollar != MENU[Type]["cost"]:
                print("Here\'s $"+str(dollar - MENU[Type]["cost"]))
            print("Here is your "+ Type +" ☕ Enjoy")



cont = True
while cont:

    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        cont = False
    elif user_input=='report':
        print("Water:" + str(resources["water"])+"ml")
        print("Milk:"+str(resources["milk"])+"ml")
        print("Coffee:"+str(resources["coffee"])+"g")
        print("Money:$" + str(resources["money"]))
    else:
        dollar = get_and_calc_money()
        requirements(dollar, user_input)








