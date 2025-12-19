import getpass

class Number:
    
    def __init__(self):
        self.number = (int(getpass.getpass("Guess a number: ")))
        
    def explaining(self):
        self.guess = int(input("guess a number: "))
        turns = 1
        while self.guess != self.number:
            if self.guess > self.number:
                print("Too high, choose a small number.\n ")
            else:
                print("Too small, Choose a high number.\n ")
            turns += 1
            self.guess = int(input("Guess again : "))
            
        return f"You win the match in {turns} turns. "
    
number = Number()
print(number.explaining())