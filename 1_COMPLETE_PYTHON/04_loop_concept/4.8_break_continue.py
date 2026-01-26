"""You want to skip those and stop entirely if someone 
requests a restricted flavor.
Taks:
"""

flavours=["Ginger","out of stock","Lemonn","Disconntinued","Tulsi"]

for flavor in flavours:
    if flavor =="out of stock":
        continue
    if flavor =="Discontinued":
        break
    print(f"{flavor} item found ")

print(f"Out side of loop.")

