from Coffee_Machine_Data import menu, resources, coins


def is_suficient(product):
    """Checks, when given a product from the menu list as input, if there's suficient resources left.
     Returns a list containing which ones are over or an empty list if everything is available."""
    current_product = menu[product]['ingredients']
    for key in current_product:
        if current_product[key] > resources[key]:
            print(f"Sorry, there is not enough {key}.")
            return False
    return True


def add_coins():
    """Asks for how many coins of each type the costumer has, returns the sum of all the amount given times the value each type has."""
    print("Please insert your coins.")
    pennies = int(input('How many pennies: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickles: '))
    quarters = int(input('How many quartes: '))
    count_of_coins = [pennies * 0.01, dimes * 0.05, nickles * 0.1, quarters * 0.25]
    return sum(count_of_coins)


def calculate_coins(inserted, choice):
    """Calculates if the amount given is higher, lower or equal to the current price of the product selected.
     Returns the calculation rounded by two decimal places (unless the amount inserted is lower than the actual price, in that case returns 0)."""
    amount = menu[choice]["cost"]
    total = 0
    if inserted > amount:
        total = inserted - amount
    elif inserted < amount:
        total = 0
    else:
        return amount
    return round(total, 2)


def make_coffee(choice):
    """Deduct the required ingredients from the resources."""
    for key in resources:
        resources[key] -= menu[choice]["ingredients"][key]
    print(f"Here is your {choice} ☕. Enjoy!")


choice = input("What would you like? (espresso/latte/cappuccino): ")
money = 0
while choice not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
while choice != 'off':
    if choice == 'report':
        print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${money}""")
    else:
        if is_suficient(choice):
            payment = add_coins()
            if calculate_coins(payment, choice) == 0:
                print("Sorry, that's not enough money. Money refunded.")
            elif calculate_coins(payment, choice) == menu[choice]['cost']:
                money += menu[choice]['cost']
                make_coffee(choice)
            else:
                money += menu[choice]['cost']
                print(f"Here is ${calculate_coins(payment, choice)} in change.")
                make_coffee(choice)
    choice = input("What would you like? (espresso/latte/cappuccino): ")


