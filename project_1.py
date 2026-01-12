#Real world use of inheritance and composition.

class Tea: 
    def __init__(self,milk = "with", strength = "normal", type_ = "regular"):
          self.milk = milk
          self.strength = strength
          self.type_ = type_
          
    def preparing(self):
         print(f"preparing {self.strength} {self.type_} chai {self.milk} milk. ")

# chai = Tea(strength="strong",type_ = "masala")
# chai.preparing()

class MasalaChai(Tea):
    
    def __init__(self, milk = "with", strength = "normal"):
        Tea.__init__(self,type_="masala", milk=milk, strength=strength)
    
    def adding_spices(self):
        print("Adding Cadmom, Elachi, Cinamon")

# masalatea = MasalaChai(milk="without", strength="strong")
# masalatea.preparing()

class LemonChai(Tea):
    
    def __init__(self, strength = "normal"):
        super().__init__(type_= "lemon",strength=strength, milk ="without")
        
    def adding_lemon(self):
        print("Adding lemon. ")

# lemontea = LemonChai()
# lemontea.preparing()       

class ChaiShop:
    Lemon = LemonChai
    Masala = MasalaChai
    Chai = Tea
    
    def dening(self,text):
        self.negetive = ['no', 'nai','ni','nope','nothing','na']
        self.changes = [change for change in text.lower().split() if change in self.negetive]
        return self.changes
    
    def __init__(self):
        self.order = input("What is your order?\n ")
        
        if "masala" in self.order.lower().split():
            self.change =input("Our default masala chai comes with milk and it is normal. Do you want any change?\n ")
            if not self.dening(self.change):
                self.milk = input("You want with milk or without milk? ")
                self.strength = input("You want less or more strength? ")
                self.chai = self.Masala(milk=self.milk, strength=self.strength)
            else:
                self.chai = self.Masala()
            
        elif "lemon" in self.order.lower().split():
            self.change=input("Our default lemon tea's strength is normal.Do you want any change?\n ")
            if not self.dening(self.change):
                self.strength = input("You want less or more strength? ")
                self.chai = self.Lemon(strength=self.strength)
            else:
                self.chai = self.Lemon()
                
        elif "chai" in self.order.lower().split() or "tea" in self.order.lower().split():
            self.change = input("Our default chai comes with milk and it's strength is normal. Do you want any change?\n ")
            
            if not self.dening(self.change): 
                self.milk = input("You want with milk or without milk? ")
                self.strength = input("You want less or more strength? ")
                self.chai = self.Chai(milk=self.milk, strength=self.strength)
            else:
                self.chai = self.Chai()
            
        else:
            print("No order available. ")
            return None
        self.chai.preparing()
        
    def serving(self):
        try:
            self.chai
            print("Serving your order. ")
        except AttributeError:
            return None
            
jina = ChaiShop()
jina.serving()    