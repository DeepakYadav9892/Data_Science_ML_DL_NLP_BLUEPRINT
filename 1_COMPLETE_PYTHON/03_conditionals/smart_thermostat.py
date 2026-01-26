"""You're building a smart thermostat aler system:
If the device_Status si active 
And temperature >35 --> Warn : High temprature alert!! 
else: the temperature is normal 

If device is off ---> Device is offline /off"""

device_status="active" #can be active or off 
temperature=38

if device_status=="active":
    if temperature>35:
        print("High temperature alert!!")
    else:
        print("The temperature is normal")
else:
    print("Device is Offline /off")
