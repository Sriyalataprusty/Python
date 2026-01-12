from menu import Menu
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "coffee": 1,
            "milk": 200
        }
        
    def report(self):
        print(f"water:{self.resources['water']} ml")
        print(f"milk:{self.resources['milk']} ml")
        print(f"coffee:{self.resources['coffee']} gm")
        
    def is_resources_sufficient(self,order):
        self.can_make = True
        for items in order.ingredient:
            if order.ingredient[items] > self.resources[items]:
                self.can_make = False
        return self.can_make
    
    def make_coffee(self,order):
        if self.is_resources_sufficient(order) == True:
            for items in order.ingredient:
                self.resources[items] -= order.ingredient[items]
            print(f"Here is your {order.name}.")
        else:
            print(f"We don't have sufficient ingredients to make {order.name} item.")
            print(f"{order.cost} refunded to source account.")
          
        

if __name__ == "__main__":
    coffee_maker = CoffeeMaker()
    coffee_maker.report()
    # print(coffee_maker.is_resources_sufficient(Menu().find_drink("latte")))
    coffee_maker.make_coffee(Menu().find_drink("espresso"))
    coffee_maker.report()