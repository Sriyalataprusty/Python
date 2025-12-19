class Bird:
    
    def __init__(self, Name, Colour, Fly):
        self.name = Name
        self.colour = Colour     
        self.fly = Fly  
          
    def guessing(self):
        self.guess = input(f"Guess the name of a bird , whose colour is {self.colour} and speed is {self.fly}.\n ")  
        
    def checking(self):
        attempt = 1
        while self.guess.lower() != self.name.lower():
            self.guess = input("Your guess is incorrect. Please try again. \n")
            attempt += 1
        return f"You guessed correctly in {attempt} attempts.This bird name is {self.name}. "
    
parrot = Bird("parrot", "Green", "Moderate")
parrot.guessing()
print(parrot.checking())