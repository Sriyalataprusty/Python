import getpass

class Bird:
    
    def __init__(self):
        self.name = getpass.getpass("What is the name of the bird?\n ")
        self.colour = getpass.getpass("What is the colour of the bird?\n ")
        self.fly = getpass.getpass("What is the speed of the bird?\n ")
          
    def guessing(self):
        self.guess = input(f"Guess the name of a bird , whose colour is {self.colour} and speed is {self.fly}. \n ")  
        
    def checking(self):
        attempt = 1
        while self.guess.lower() != self.name.lower():
            self.guess = input("Your guess is incorrect. Please try again. \n")
            attempt += 1
        return f"You guessed correctly in {attempt} attempts.This bird name is {self.name}. "
    
bird = Bird()
bird.guessing()
print(bird.checking())