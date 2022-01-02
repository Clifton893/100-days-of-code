from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Program Requirements
# 1. Print report ✅
# 2. Check if resources are sufficient ✅
# 3. Process coins ✅
# 4. Check if transaction is successful ✅
# 5. Make coffee ✅

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}) \n")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
