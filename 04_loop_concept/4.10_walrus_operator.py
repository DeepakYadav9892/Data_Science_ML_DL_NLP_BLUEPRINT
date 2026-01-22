"""Walrus operator allows assignment expressionns inside expressions
"""

value=13
remainder=value%2
if remainder:
    print(f"Not divisible , remaindes is {remainder}")



value=13
if (remainder:=value%5):
    print(f"Not divisible, reaminders is {remainder}")

available_sizes=["small","medium","large","extra large"]
if(requested_size:=input("Enter your chai cup size:") in available_sizes):
    print(f"serving chai in {requested_size} cup")
else:
    print(f"Size is unavailable --{requested_size}")   

flavours=["Masala","Ginger","Lemon","Mint"]
print("Available flavours are:",flavours)
while(flavor:=input("choose your flavor:")) not in flavours:

    print(f"Sorry,{flavor} is nnot availbale")
print(f"You choose {flavor}chai")