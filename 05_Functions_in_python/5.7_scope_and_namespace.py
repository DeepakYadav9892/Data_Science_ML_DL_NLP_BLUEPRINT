"""Scopes and namespaces in python """

#Global scope and local scope 
## Scope refers to the visiblity of variables 
## Scopes and name Resolution 

##Local -inside function , Enclosing function  outer function if nested 
##Global -Top level script or module 

def serve_chai():
    chai_type="Masala chai" #local scope 
    print(f"Serving chai inside function:{chai_type}")

chai_type="Lemon ginger chai"
serve_chai()
print(f"Outside function chai :{chai_type}")


def chai_counter():
    chai_order="lemon ginger chai"
    print("Inner:",chai_order)

    def print_order():
        print("Inner:",chai_order)
    print_order()
    print("Outer:",chai_order)

    