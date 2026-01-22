"""
Docstring for 05_Functions.5.10_return
I will return you this value 

Nothing ---> Implicitly returns None
One value 
multiple value 
early from a function 
"""


# def make_chai():
#     return "here is your masala chai"


# return_value=make_chai()
# print(return_value)
# print(make_chai())

def idle_chaiwala():
    pass
print(idle_chaiwala())

def sold_cups():
    return 120

total=sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left==0:
        return "Sorry , chai is over "
    return "chai is ready "

print(chai_status(0))
#print(chai_status(5))

def chai_report():
    return 100,20 #sold,reamining 
sold,remaining =chai_report()
print("Sold:",sold)
print("Remaining:",remaining)