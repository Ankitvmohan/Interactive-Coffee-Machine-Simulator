menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "cost": 1.50
    },
    
    "latte":{
        "ingredients":{
            "milk": 150,
            "water": 200,
            "coffee": 24
        },
        "cost": 2.50
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.00
    }
}

profit = 0
resources = {
    "milk":500,
    "water": 500,
    "coffee": 70
}

def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        """returns true when the ordered made has the right amount of ingredients, and False if they aren't sufficient"""
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough of {item}.")
            return False
    return True

def process_coins():
    """returns the total set of change after asking for the coins"""
    print("Please insert coins: ")
    total = int(input("How many quarters are there: "))*0.25
    total += int(input("How many dimes are there: "))*0.10
    total += int(input("How many nickles are there: "))*0.05
    total += int(input("How many pennies are there: "))*0.01
    return total

def is_transaction_Successful(money_recieved, cost_drink):
    if money_recieved >= cost_drink:
        change = round(money_recieved - cost_drink,2)
        print(f"Here is your change: ${change}")
        global profit
        profit += cost_drink
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the amount of ingredients that is required for the drink"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee {drink_name}") 
        
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}ml"),
        print(f"Water: {resources['water']}ml"),
        print(f"Coffee: {resources['coffee']}g"),
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_Successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])