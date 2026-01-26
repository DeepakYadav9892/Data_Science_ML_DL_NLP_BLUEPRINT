"""
Docstring for 07_comprehensions.7.0_

Comprehensionns are a concise way to create 
lists,
sets, 
dictionaries, 
or generators in python using a single line of codde 


where they are used in real life . ?

filter item 
tranform  item 

create a new collection 
flatten nested structure 




List [expression for item in iterable if condition]

"""

menu=[
    "Masala chai",
    "Iced lemon tea",
    "Green Tea",
    "Iced peach tea",
    "Ginger chai "
]

iced_tea=[tea for tea in menu if len(tea)>10]

print(iced_tea)


