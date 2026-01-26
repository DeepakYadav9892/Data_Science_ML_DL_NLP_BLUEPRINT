"""
Docstring for loop_concept.02_tea_token_dispenser
A tea stall owner has a digital token display.
For every customer, a token number is printed and chai is served.
Task:
Use a for loop to generate token numbers from 1 to 10 using 
range().
Print: Serving chai to token number:<token_number>
"""

for token_number in range(1,11):
    print(f"Serving chai to token number:{token_number}")