import math 
from ExperimentalData import ExperimentalData

# gun = "Vpr-Hunter"
# cartridge = "7.62x51mm"
# ammunitionType = "7.62x51mm FMJ"
# velocity = 840.00
# buildingName = "Miramar Plaza Center"
# buildingHeight = 78.33


def calculateProjectileMotion(experimentalData: ExperimentalData):
    #calculate the time it will fly for
    time = math.sqrt((2* experimentalData.buildingHeight / experimentalData.gravity))
    #calculate the distance using the calculated time and velocity
    distance = experimentalData.velocity*time
  
    print(f"The gun is the {experimentalData.gun}. The cartridge is the {experimentalData.cartridge} and its ammunition type is {experimentalData.ammunitionType}. The velocity of the the bullet is {experimentalData.velocity}m/s. If I shoot from the top of {experimentalData.buildingName} and its height is {experimentalData.buildingHeight}m. Taking in to consideration that there isnt any air resistance and the height of the building, the time traveled is {time}s and the distance traveled would be {distance}m")

myData = ExperimentalData("Vpr-Hunter", "7.62x51mm", "7.62x51mm FMJ", 840.00, "Miramar Plaza Center", 78.33, 9.8)



calculateProjectileMotion(myData)

