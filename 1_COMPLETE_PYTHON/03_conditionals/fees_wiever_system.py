"""You run an online tea store 
if the order amount is more then 300 , delivery 
is free 
otherwise , it costs 30 rupees 

task 
input : order_amount 
use ternary operator to determine delivery fee"""


order_amount=input("Enter the order amount : ")
print(f"Order amount:{type(order_amount)}")
order_amount=int(order_amount)

delivery_fee=0  if order_amount >300 else 30 
print(f"Delivery fee is : {delivery_fee}")

