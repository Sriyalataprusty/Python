#Inheritance

class Ghusuri: 
    
    def __init__(self):
        self.food = "poop"
        self.favourite_palce = "dirty place"
    
    def eating(self):
        print(f"ghusuri eats : {self.food}")

class Anita(Ghusuri): 
    
    def favourite_work(self,name):
        print(f"Anita is quarrelling with {name}.")
    
kodi = Anita()
kodi.eating()
kodi.favourite_work("mihir") # As anita is a ghusuri that's why it works.

boar = Ghusuri()
boar.eating()
# boar.favourite_work("Tuin") # Ghusuri is not a anita that's why it gives error.