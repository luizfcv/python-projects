from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker1 = CoffeeMaker()
menu1 = Menu()
money_machine1 = MoneyMachine()

is_on = True
while is_on:
    options = menu1.get_items()
    order = input(f"What would you like? ({options}): ")
    while order not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        menu1.find_drink(order)
        order = input(f"What would you like? ({options}): ")
    if order == 'off':
        is_on = False
    elif order == 'report':
        coffee_maker1.report()
        money_machine1.report()
    else:
        drink = menu1.find_drink(order)
        resources_sufficient = coffee_maker1.is_resource_sufficient(drink)
        cost = drink.cost
        money_received_is_sufficient = money_machine1.make_payment(cost)
        if resources_sufficient and money_received_is_sufficient:
            coffee_maker1.make_coffee(drink)






