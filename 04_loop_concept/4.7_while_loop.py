"""While loops in Python
A while loop repeatedly executes a block of code as long as a"condition is true
You want to simulate tea heating . 
It starts at 40 degrees celsius and boils at 100 degrees celsisus
Task:
Use a while loop .
increase temperature by 15 until it reaches or exceeds 100.
print each temperature step.



"""

temperature=40
while temperature<100:
    print(f"Current temperature:{temperature}")
    temperature+=15
print("Tea is ready to boil!Enjoyy your hot tea!")
