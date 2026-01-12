# Static method
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
    chai = input("what type of chai you want? ")
    @classmethod
    def pourine_chai(cls):
        print(f"pouring {cls.chai} chai. ")
        
    def __init__(self, milk = "with", strength = "normal"):
        Tea.__init__(self,type_="masala", milk=milk, strength=strength)
    @classmethod
    def adding_spices(cls):
        print("Adding Cadmom, Elachi, Cinamon")

# masalatea = MasalaChai(milk="without", strength="strong")
# masalatea.preparing()
MasalaChai.adding_spices()
#MasalaChai.pourine_chai()