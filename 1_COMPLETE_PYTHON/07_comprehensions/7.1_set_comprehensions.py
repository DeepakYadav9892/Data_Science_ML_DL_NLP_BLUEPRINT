"""
Docstring for 07_comprehensions.7.1_set_comprehensions
{expression for item in iterable if  condition }

"""
favourite_chais=[
    "Masala chai","Green Tea","Masala chai",
    "Lemon tea","Green tea","Elaichi chai"
]

unique_chai={chai for chai in favourite_chais if len(chai)>8}
print(unique_chai)

recipes={
    "Masala Chai":["ginger","cardmom","clove"],
    "Elaichi chai":["cardamom","milk"],
    "Spicy chai":["ginger","black pepper","clove"],
}

unique_spices={spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)

