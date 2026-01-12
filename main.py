from menu import Menu
from coffemaker import CoffeeMaker
from money_counter import MoneyCounter

is_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
payment = MoneyCounter()

while is_on:
    options = menu.get_item()
    choice = input("What do you want to purchase?\n")
    
    if choice == "off":
        is_on = False
        print("Machine is off.\n")
    elif choice == "report":
        coffee_maker.report() 
        payment.report()
    else:
        drink = menu.find_drink(choice)
        if drink and payment.upi_payment(choice):
            coffee_maker.make_coffee(drink)
           