from menuRes import MENU, resources


quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01
cont = True
profit = 0

def espresso():
    global profit
    if resources["water"] > MENU[choice]["ingredients"]["water"]:
        if resources["coffee"] > MENU[choice]["ingredients"]["coffee"]:
                    
                    q = int(input("Please insert coins.\nHow many quarters?: "))
                    d = int(input("How many dimes?: "))
                    n = int(input("How many nickles?: "))
                    p = int(input("How many pennies?: "))
                    paid = [q*quarter, d*dime, n*nickel, p*penny]
                    change = sum(paid) - MENU[choice]["cost"]

                    if sum(paid) >= MENU[choice]["cost"]:
                        print(f"\nHere is ${change} in change.\nHere is your {choice}☕️. Enjoy!\n")
                        resources["water"] -= MENU[choice]["ingredients"]["water"]
                        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                        profit += sum(paid) - change

                    else:
                        print("Sorry that's not enough money. Money refunded.")
                        cont = False
        else: 
            print("Not enough coffee.")
    else:
        print("Not enough water.")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}\n")

def latcap():
    global profit
    if resources["water"] > MENU[choice]["ingredients"]["water"]:
        if resources["milk"] > MENU[choice]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[choice]["ingredients"]["coffee"]:
                
                q = int(input("Please insert coins.\nHow many quarters?: "))
                d = int(input("How many dimes?: "))
                n = int(input("How many nickles?: "))
                p = int(input("How many pennies?: "))
                paid = [q*quarter, d*dime, n*nickel, p*penny]
                change = sum(paid) - MENU[choice]["cost"]

                if sum(paid) >= MENU[choice]["cost"]:
                    print(f"\nHere is ${change} in change.\nHere is your {choice}☕️. Enjoy!\n")
                    resources["water"] -= MENU[choice]["ingredients"]["water"]
                    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                    profit += sum(paid) - change

                else:
                    print("Sorry that's not enough money. Money refunded.")
                    cont = False
                

            else: 
                print("Not enough coffee.")
        else:
            print("Not enough milk.")
    else:
        print("Not enough water.")


while cont == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'report':
        report()      

    elif choice == 'off':
        cont = False

    elif choice == 'espresso':
         espresso()

    else:
        latcap()