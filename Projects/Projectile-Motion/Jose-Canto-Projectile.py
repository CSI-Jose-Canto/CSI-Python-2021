import math 

gun = "Vpr-Hunter"
cartridge = "7.62x51mm"
ammunitionType = "7.62x51mm FMJ"
velocity = 840.00
buildingName = "Miramar Plaza Center"
buildingHeight = 78.33

#calculate the time it will fly for
time = math.sqrt((2*buildingHeight)/9.8)
#calculate the distance using the calculated time and velocity
distance = velocity*time

print(f"The {gun} has a cartridge of {cartridge} and ammunition type of {ammunitionType}. The velocity for this bullet is {velocity}m/s. If I fire from the top of {buildingName} at a hieght of {buildingHeight}m, then the bullet will fly for {distance}m.")
