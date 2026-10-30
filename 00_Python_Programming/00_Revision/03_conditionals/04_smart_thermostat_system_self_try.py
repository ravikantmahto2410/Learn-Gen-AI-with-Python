## Problem Statement
## You are building a thermostat alert system : 
 # If the  Device Status is "active"
 # And temperature > 35 -> Warn : "High Temperature"
 # Else : "Temperature Normal"

 # If device is off --> "Device is Offline"

status = "offline"
temperature = 20

if status == "active":
    if temperature > 35:
        print(f"High Temperature")

    else:
        print(f"Temperature Normal")

else:
    print(f"Device Offline")