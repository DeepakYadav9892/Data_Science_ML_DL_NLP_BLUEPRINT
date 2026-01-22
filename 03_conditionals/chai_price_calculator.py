"""A tea stall offers different prices for different cups
sizes. Write a program that calcualtes the price based on size.
Task:
Input : small , medium, large
small --> 10, medium -->15 , large --->20
if invalid : show "Unknown cup size """

cup_size=input("Welcome to tea stall!! What cup size would you like to order?(small/medium/large)".lower())

if cup_size=="small":
    print("the price for small cup is 10 rupees")
elif cup_size=="medium":
    print("the price fo the medium cup is 15 rupees")
elif cup_size=="large":
    print("the price of the large size cup is 20 rupees")
else:
    print("Unknown cup size")

