from data import MENU,resources,logo

def availableRes(orderedRes):
    for items in orderedRes:
        if orderedRes[items]>=resources[items]:
            print(f"Sorry!There is a shortage of {items}")
            return False
        return True

def coins():
    print("please insert coins.")
    total=int(input("How many quarters?: ")) * 0.25
    total+=int(input("How many dimes?: ")) * 0.1
    total+=int(input("How many nickles?: ")) * 0.05
    total+=int(input("How many pennies?: ")) * 0.01
    return total

def transaction(payment,cost):
    if payment>=cost:
        change=payment-cost
        global profit
        profit+=cost
        print(f"Here is Your ${round(change,2)} change")
        return True
    else:
        print(f"Sorry!Insufficient funds.${payment} refunded")
        return False

def prepareCoffee(drink,required):
    for items in required:
        resources[items]-=required[items]
    print(f"Here is Your {drink}")

isOn=True
profit=0

print(logo)
while isOn:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        isOn=False
    elif choice=="report":
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"profit ${profit}")
    else:
        drink=MENU[choice]
        if availableRes(drink["ingredients"]):
            payment=coins()
            if transaction(payment,drink["cost"]):
                prepareCoffee(choice,drink["ingredients"])
