class Animal:
    
    def __init__(self, name):
        self.name = name 
    
    def reproducing(self):
        print(f"{self.name} give birth to its own type. ")
        
class Pig(Animal):
    
    def cleaning_gutter(self):
        print(f"{self.name} is eating poop to clean the gutter. ")

# kodi = Pig("kodi")
# kodi.cleaning_gutter()
# kodi.reproducing()   

class Tuin(Animal):
    kodi = Pig
    
    def working(self):
        self.anita = self.kodi("Anita")
        self.anita.cleaning_gutter()
        
sriya = Tuin("Sriya")
sriya.working()
sriya.reproducing()
sriya.anita.reproducing()