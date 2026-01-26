sugar_amount=1000
print("sugar_amount=",sugar_amount)

sugar_amount=500
print("sugar_amount=",sugar_amount)

## we are changing the reference of sugar_amount 
print(f"Id Of 2:{id(sugar_amount)}")

"""Common Immutable Types

int

float

bool

str (string)

tuple

frozenset"""
x = 10
x = x + 5
print(x)
# Here, the value of x is changed from 10 to 


# 15 by creating a new integer object and updating the reference of x to point to this new object.


""""Mutable types 
List
Dict
set 
bytearray
"""
nums = [1, 2, 3]
nums[0] = 10
print(nums)
# Here, the first element of the list nums is changed from 1 to 10 without creating a new list object.