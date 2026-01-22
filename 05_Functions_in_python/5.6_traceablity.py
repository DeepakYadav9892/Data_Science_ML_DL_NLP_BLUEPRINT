"""
Docstring for 05_Functions.5.6_traceablity
Your shop adds a 10% VAT onn every order.
you want this to be consistent and traceabble .
Task:
Write add_vat(price,vat_rate)
use it to compute final prices for 3 orders 

"""

def add_vat(price,vat_rate):
    return price *(100+vat_rate)/100


orders=[100,200,250]
for price in orders:
    final_amount=add_vat(price,10)
    print(f"Original values:{price},final with VAT :{final_amount}")