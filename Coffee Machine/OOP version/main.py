from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# moneyMachine=MoneyMachine()

# coffeeMaker=CoffeeMaker()

# menu=Menu()

# isOn=True

# while isOn:
#     options=menu.get_items()
#     choice=input(f"What would You Like ({options}): ")
#     if choice=="off":
#         isOn=False
#     elif choice=="report":
#         coffeeMaker.report()
#         moneyMachine.report()
#     else:
#         drink=menu.find_drink(choice)
#         if coffeeMaker.is_resource_sufficient(drink):
#            if moneyMachine.make_payment(drink,drink.cost):
#                 coffeeMaker.make_coffee(drink)

            
menu=Menu()
moneyManchine=MoneyMachine()
coffeeMaker=CoffeeMaker()

isOn=True

while isOn:
    options=menu.get_items()
    choice=input(f"What would you like ({options}): ")
    if choice=="off":
        isOn=False
    elif choice=="report":
        coffeeMaker.report()
        moneyManchine.report()
    else:
        drink= menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyManchine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)


