class Chai:
    temprature="hot"
    strength="Strong"

cutting=Chai()
print(cutting.temprature)
cutting.temprature="Mild"
cutting.cup="small"
print("After changing",cutting.temprature)
print("cup size is ",cutting.cup)
print("Direct look into the class",Chai.temprature)

del cutting.temprature
del cutting.cup
print(cutting.temprature)