# Initialization
class Animal:
    
    def __init__(self, size, food, name):
        self.size = size
        self.food = food
        self.name = name
    
    def explaining(self):
        return f"It is an animal who eats {self.food} and it's size is {self.size}. "
    
    def guessing(self):
        self.guessed_name = input("Guess the name of the animal\n ")
        if self.guessed_name.lower() == self.name.lower() :
            return f"You guessed the correct one. It is a {self.name}. "
        else:
            return f"You lost, It is not a {self.guessed_name}, it is a {self.name}. "

tuin =  Animal("Small", "Nuts", "Squirrel")
mihir = Animal("Small", "Grain", "Rat")
anita = Animal("Medium","Poop", "Pig" )
print(tuin.explaining())
print(tuin.guessing())

print(mihir.explaining())
print(mihir.guessing())

print(anita.explaining())
print(anita.guessing())