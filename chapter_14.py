# property decorater or getter setter
from datetime import date
class EligibilityError(Exception):
    pass
class Voter:
    
    def __init__(self):
        self._name = input("What is your name?\n")
        self._adhar_no = int(input("what is your Adhar no.?\n"))
        self._age = int(input("What is your age?\n"))
        self._adress = input("What is your adress?\n")
        self.age_validation = self._age
    
    @property
    def age_validation(self): # getter
        return self._age
    
    @age_validation.setter
    def age_validation(self, value):
        if value < 18:
            raise EligibilityError("You are under age to be registered.")
        else:
            self._age = value

voter_1 = Voter()
print(voter_1._age)