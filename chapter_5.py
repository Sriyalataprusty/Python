# dunder doc or built in function
def eating(name, food):
    """
    It returns who eats what.
    """
    return f"{name} eats {food}"

print(eating("pig", "poop"))
print(eating.__doc__)