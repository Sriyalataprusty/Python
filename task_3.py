import random

class Number:
    
    def explaining(self):
        self.random_num = random.randint(1, 101)
        self.guess = int(input("guess a number: "))
        turns = 1
        while self.guess != self.random_num:
            if self.guess > self.random_num:
                print("Too high, choose a small number.\n ")
            else:
                print("Too small, Choose a high number.\n ")
            turns += 1
            self.guess = int(input("Guess again : "))
        return f"you win the match in {turns} turns. "

number = Number()
print(number.explaining())