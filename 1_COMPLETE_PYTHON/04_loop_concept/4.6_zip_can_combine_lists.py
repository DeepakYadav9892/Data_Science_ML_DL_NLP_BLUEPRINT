"""

You are preparing an order summary with customer 
names and their total bill. 

Task:
SUe two lists: one for names adn one for 
bills.
Print:"[Name] paid rupees [amount]

"""

names=["Deepak","ravi","Anjali","shivam"]
bills=[120,150,100,130]
for name,amount in zip(names,bills):
    print(f"{name} paid rupes {amount}")
