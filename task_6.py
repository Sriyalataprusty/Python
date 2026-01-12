from functools import wraps
def position(function):
    @wraps(function)
    def wrapper(required_role):
        position = input("Who is this?\n")
        if position != required_role:
            print(f"no acess! {required_role} only. ")
        else:
            return function()
    return wrapper

@position
def admin_page(required_role = "admin"):
    print("admin page.")
@position    
def order_page(required_role = "waiter"):
    print("Waiter page.")
@position
def order_menu(required_role = "customers"):
    print("order menu. ")
    
admin_page(required_role="Sriya")
#order_page(required_role="waiter")