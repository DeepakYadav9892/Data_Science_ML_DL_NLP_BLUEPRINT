"""A local cafe wants a program that suggests a snack .
IF a customer asks for cookies or samosa, it connfirms teh order.
Otherwise, it says its not available.
Task:
take snack input 
if its "cookies" or "samosa",confirm the order 
Else, show unvailaility messages.

"""
snack=input("Wellcome to cafe! What snack would you like to ordrer?")
print(f"user said:{snack}")

if snack=="cookies" or snack=="samosa":
    print(f"Great choice! we'll serve you {snack}")
else:
    print(f"sorry, we only serve cookies or samosa with tea")

