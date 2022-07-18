#Fix Required
# 1.Insufficient fund/coins --> No utilisation of Resources.No drink!
# 2.Insufficient resource --> No Payment Prompt
# 3.use Resource dictorary from Data.py
from data import MENU as menu

def require(menu,order):
    ingredients=menu[order]["ingredients"]
    cost=menu[order]["cost"]
    return ingredients,cost

def check(Milk,Water,Coffee,milk,water,coffee):
    if Milk<milk or Milk==0:
        print("sorry!But there isnt enough Milk in the unit")
    elif  Water<water or Water==0:
        print("sorry!But there isnt enough Water in the unit")
    elif Coffee<coffee or Coffee==0: 
        print("sorry!But there isnt enough coffee in the unit")
    else:
        return False

#Temporary Fix
def unit(Water,Milk,Coffee):
    if Water<40 or Milk<40 or Coffee<15:
        print("Sorry!There is Shortage of Supply")
    else:
        return False

Water=300
Milk=200
Coffee=100
Money=0

manchineON=True


while manchineON:

    order=input("What would you like? (espresso/latte/cappuccino):").lower()
    if order=="report":
        print(f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}g\nMoney: ${Money}")
        manchineON=False
    elif order=="espresso":    
        items=require(menu,order)[0]
        Cost=require(menu,order)[1]
        water=items["water"]
        coffee=items["coffee"]
        milk=0
        if check(Milk,Water,Coffee,milk,water,coffee)==False:
            Water-=water
            Coffee-=coffee
            Money+=Cost
    elif order=="cappuccino":
        items=require(menu,order)[0]
        Cost=require(menu,order)[1]
        milk=items["milk"]
        water=items["water"]
        coffee=items["coffee"]
        if check(Milk,Water,Coffee,milk,water,coffee)==False:
            Milk-=milk
            Water-=water
            Coffee-=coffee
            Money+=Cost
    elif order=="latte":
        items=require(menu,order)[0]
        Cost=require(menu,order)[1]
        milk=items["milk"]
        water=items["water"]
        coffee=items["coffee"]
        if check(Milk,Water,Coffee,milk,water,coffee)==False:
            Milk-=milk
            Water-=water
            Coffee-=coffee
            Money+=Cost
    elif order=="off":
        manchineON=False

    if manchineON:
        if unit(Water,Milk,Coffee)==False:
            Cost=require(menu,order)[1]
            print("please Insert coins")
            pennies=int(input("How many pennies?: "))*0.01
            dimes=int(input("How many dimes?: "))*0.1
            quarters=int(input("How many quaters?: "))*0.25
            nickel=int(input("How many pennies?: "))*0.05
            coins=quarters+dimes+pennies+nickel
            if coins>Cost:
                change=coins-Cost
                print(f"Here is ${round(change,2)} in change")
            elif coins<Cost:
                print(f"Sorry insufficient Fund!Amount {round(coins,2)} refunded")
            else:
                print("Thank You!Enjoy Your Coffee")
