## method inside class
from types import MethodType

class Ghusuri:
    colour = "black"
    face = "cylindrical"
    hair = "curly"
    food = "poop"

    def eating(self): # instance method
        return f"Ghusuri is eating: {self.food}"

anita = Ghusuri()
kodi = Ghusuri()
print(anita.eating())
anita.food = "fresh poop"
print(anita.eating())

def walking(self):
    return f"walking on 2 legs"
anita.walking = MethodType(walking, anita)
print(anita.walking())
#print(kodi.walking()) # error bcoz walking is only used for anita

def add(a, b): # method or function
    print(a+b)
add(2,3)