from coffeemachine import *
import signal
import sys
import readchar
import copy

menu = coffeemenu
resources = resources
coins = coins

def handler(signum, frame):
    msg = "\n\nCtrl-c was pressed. Do you really want to exit? y/n: "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)
 
def report(func):
    def wrapper(arg):
        func(arg)
    return wrapper

@report
def print_report(resources):
    index = 1
    for key, value in resources.items():
        if type(value) == type({}):
            """
            # if value is a dict type then
            # FIRST: print index of resource
            # SECOND: the 'value' which is dict type, pass to the 
            # 
            # print_report( value -> resources) 
            # and again check
            # if the resources have a dict type
            """
            print(f"{index}.{key}:", end=" ")
            print_report(value)
        else:
            """# if resources is NOT a dict type then print the value"""
            print(f"{value} ", end="")
        index += 1 
    print("") 

def checkTypeInputMoney(money) -> bool:
    if money.isnumeric():
        if int(money) != 0:
            return int(money)
    return False

def take_money(resources):
    try:
        quarters = checkTypeInputMoney( input("How many quarters?: ") )
    except ValueError and EOFError:
        pass
    try:
        dimes =  checkTypeInputMoney( input("How many dimes?: "))
    except ValueError and EOFError:
        pass
    try:
        nickles = checkTypeInputMoney( input("How many nickles?: "))
    except ValueError and EOFError:
        pass
    try:
        pennies = checkTypeInputMoney( input("How many pennies?: "))
    except ValueError and EOFError:
        pass
    
        while not quarters or not dimes or not nickles or not pennies:  
            print("[Error]: Money must be integer number and can't be zero!")
            if not quarters:
                try:
                    quarters = checkTypeInputMoney( input("How many quarters?: ") )
                except ValueError and EOFError:
                    pass
            elif not dimes:
                try:
                    dimes =  checkTypeInputMoney( input("How many dimes?: "))
                except ValueError and EOFError:
                    pass
            elif not nickles:
                try:
                    nickles = checkTypeInputMoney( input("How many nickles?: "))
                except ValueError and EOFError:
                    pass
            elif not pennies:
                try:
                    pennies = checkTypeInputMoney( input("How many pennies?: "))
                except ValueError and EOFError:
                    pass
    
    quarters = quarters * coins["Quarter"]
    dimes = dimes * coins["Dime"]
    nickles = nickles * coins["Nickel"]
    pennies = pennies * coins["Penny"]
    
    resources['money']['amount'] = round(sum([quarters, dimes, nickles, pennies]), 2)
    return resources['money']['amount']

def get_prices_list_coffee(menu):
    pricesListOfDict = [ { "name":menu[key]["name"] ,"price": menu[key]["price"] } for key, value in menu.items() ]
    return pricesListOfDict

def get_sum_price_all_coffee(menu):
    allCoffeePrice = sum([ x["price"] for x in get_prices_list_coffee(menu) ])
    return allCoffeePrice

def get_max_price_coffee(menu):
    maxCoffeePrice = max([ x["price"] for x in get_prices_list_coffee(menu) ])
    return maxCoffeePrice 

def get_min_price_coffee(menu):
    maxCoffeePrice = min([ x["price"] for x in get_prices_list_coffee(menu) ])
    return maxCoffeePrice 


def enough_money(money, whishes, menu) -> bool:
    allCoffeWithPrice = get_prices_list_coffee(menu)
    findedPriceCoffee = [ coffee["price"] for coffee in allCoffeWithPrice if coffee["name"] == whishes][0]
    if money < get_min_price_coffee(menu):
        return False
    elif money < findedPriceCoffee:
        return False
    return True

def process_resources(resources, whishes, menu, money):
    
    foundCoffee = menu[whishes]["ingredients"] 
    countResources = lambda ingredient, amount: resources[ingredient]["amount"] - amount 
    currentResources = [ [ { ingredient: { "amount": countResources(ingredient, amount)}} for ingredient, amount in coffee.items() if ingredient != 'unit'][0] for coffee in foundCoffee]
    for resource in currentResources:
        for element, value in resource.items():
            resources[element]["amount"] = value["amount"]
    resources["money"]["amount"] = money
    return resources
    
    
def check_resources(resources, whishes, menu):
    check_water = resources["water"]["amount"]
    check_coffee = resources["coffee"]["amount"]
    check_milk = resources["milk"]["amount"]
    check_sugar = resources["sugar"]["amount"]
    condition_water = check_water >= menu[whishes]["ingredients"][0]["water"]
    condition_coffee = check_coffee >= menu[whishes]["ingredients"][1]["coffee"]
    condition_milk = check_milk >= menu[whishes]["ingredients"][2]["milk"]
    condition_sugar = check_sugar >= menu[whishes]["ingredients"][3]["sugar"]
    
    if condition_water and condition_coffee and  condition_milk and condition_sugar:
        return True

def cash_register(money, whishes, menu):
    allCoffeWithPrice = get_prices_list_coffee(menu)
    findedPriceCoffee = [ coffee["price"] for coffee in allCoffeWithPrice if coffee["name"] == whishes][0]
    return round(money - findedPriceCoffee, 2)

print("Welcome!!!")


whishes = "menu"
while whishes != 'exit':
    match whishes:
        case 'report':
            print("=========================================")
            print("\t\tREPORT")
            print("=========================================")
            print_report(resources)
        case 'menu':
            # I don't want to operate on original dictionary 
            copyMenu = copy.deepcopy(menu)
            def createMenu(dictionary, want=[], key=''):
                createNewDict = {}
                for k, v in dictionary.items():
                    if isinstance( v, dict ):
                        createMenu(v, want, k)
                    else:
                        if k in want: 
                            createNewDict[k] = v
                if len(createNewDict):
                    createMenu.coffeeMenu.append(createNewDict)   
                                                           
            createMenu.coffeeMenu = []
            createMenu(copyMenu, ['name', 'price','unit']) 
            # createMenu( dictionary, list[of, keys, which, I want, to,take, into, account] )

            def showCoffeeMenu(coffeeList):
                index = 1
                print("=========================================")
                print("\t\tMENU")
                print("=========================================")
                
                for coffee in coffeeList:
                    print(f"{index} {coffee['name']} {coffee['price']}{coffee['unit']}")
                    index += 1
            showCoffeeMenu( createMenu.coffeeMenu )
            
        case 'latte' | 'cappuccino' | 'espresso' | 'frappe':
            
            if not check_resources(resources, whishes, menu):
                print("============== Fail order =================")
                print("Sorry... I don't have enough sufficient")
                print("===========================================")
                whishes = 'report'
                continue
            
            money = take_money(resources)
            # I need to check amount of money If money amount is below
            # than minimal coffee price, then will raise an error
            print("Your all money =", money, "$ ")
            if not enough_money(money, whishes, menu):
                print("============== Fail order =================")
                print("[Error]: You haven\'t enough money amount! ")
                print("===========================================")
                print(f"Your credit: {resources['money']['amount']} ")
                whishes = 'menu' 
                continue
            else:
                change_money = cash_register(money, whishes, menu) 
                resources = process_resources(resources, whishes, menu, change_money)
                print("")
                print(f"Here is your coffee: ☕")
                print(f"Here is { change_money }$ in change.")
                print("")

        case 'exit':
            print("Have a nice day!")
        
        case _:
            print("Wrong option, try again!")
            
    print("Type 'menu' if you would see the menu of coffee machine")
    print("Type 'report' if you would see the contents of the machine")
    
    try:
        signal.signal(signal.SIGINT, handler)
        whishes = input("What would you like? (espresso/latte/cappuccino): ")
    except ValueError and EOFError:
        pass

else:
    print("Have a nice day!")
