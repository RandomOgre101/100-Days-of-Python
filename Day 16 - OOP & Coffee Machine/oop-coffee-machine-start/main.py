from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cont = True
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

while cont == True:
    choice = input(f"What would you like? {Menu().get_items()}: ")

    if choice == 'report':
         coffee_maker.report()
         money_machine.report()

    elif choice == 'off':
         cont = False

    else:
         drink = menu.find_drink(choice)
         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
              
              

