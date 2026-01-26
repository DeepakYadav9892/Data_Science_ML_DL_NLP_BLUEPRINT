from functools import wraps
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role!="Admin":
            print("Access denied :Admin onlu")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")
acess_tea_inventory("user")
acess_tea_inventory("Admin")