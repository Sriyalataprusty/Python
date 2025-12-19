# Type of function
def pig_eating():
    food = "poop" # Local Scope because food = poop only inside pig eating.
    return f"Ghusuri eats: {food}"
print(pig_eating())

food = "rice" # Global scope because food = rice for everywhere.

def eating():
    food = "curry" # Nonlocal Scope bcoz it is neither global nor local for tuin_eating().
    print(f"Only eats before tuin_eating(): {food}")
    def tuin_eating():
        nonlocal food 
        food = "chips" # it doesn't define a new variable food inside tuin_eating() it changed the variable food from curry to chips inside eating().
        print(f"Tuin eats: {food}")
    tuin_eating() # It is a impure function bcoz it affect the nonlocal scope.
    print(f"Only eats after tuin_eating(): {food}")
eating() # it is a pure function bcoz it doesn't affect any scope outside the function.

def tuan_eating(): # We can define it again bcoz there was no existance of tuin_eating() (The function inside eating()).
    print(f"Tuan eats: {food}")
tuan_eating()

def kodi_eating():
    global food 
    food = "dal" # it doesn't define a new variable food inside kodi_eating() it changed the variable food from rice to dal global food.
    print(f"Kodi eats: {food}")
kodi_eating() # It is a impure function bcoz it affect the global scope.

print(f"Everyone eats: {food}")