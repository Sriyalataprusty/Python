class MenuItem:
    def __init__(self,name,water,milk,coffee,cost):
        self.name = name
        self.ingredient = {
            "water": water,
            "milk": milk,
            "coffee":coffee}
        self.cost = cost

class Menu:
    item = MenuItem
    def __init__(self):
        self.espresso = self.item(name="espresso", milk=0,water=50,coffee=10,cost=150)
        self.latte = self.item(name="latte", milk=50,water=250,coffee=24,cost=250)
        self.cappucino= self.item(name="cappucino", milk=50,water=250,coffee=24,cost=300)
        self.menu = [
            self.espresso,
            self.cappucino,
            self.latte
        ]
        
    def get_item(self):
        for items in self.menu:
            print(items.name,":", items.cost, "rupees. ")
            
    def find_drink(self,order):
        for items in self.menu:
            if items.name == order:
                return items
        print("Sorry! That item is not available.\n")
        
    
    
    
    
if __name__ == "__main__":   
    menu = Menu()
    print(menu.find_drink("latte"))