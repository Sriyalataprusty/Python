# Decorator
from functools import wraps
def ghusuri(function):
    @wraps(function)
    def wrapper():
        print("before running the function.")
        function()
        print("after running the function.")
    return wrapper

def may_I_go_to_toilet(function):
    def seeking_permission():
        permission = input("May I go to toilet ?\n")
        if permission.lower() == "yes":
            function()
        else:
            print("band karo! band karo! Khule mai hagna band karo.")
    return seeking_permission

@may_I_go_to_toilet
def hagiba():
    name = input("kie haguchi ?\n")
    print(f"{name} haguchi.")

# hagiba()    

@ghusuri
def mutiba():
    name = input("kie mutuchi ?\n")
    print(f"{name} mutuchi.")

mutiba()

@ghusuri
def khaiba():
    name = input("kie khauchi ?\n")
    food = input("kn khauchi ?\n")
    print(f"{name} {food} khauchi.")

khaiba()
print(khaiba.__name__)

@ghusuri
def Dance():
    print("Let's start the dance.")
Dance()    