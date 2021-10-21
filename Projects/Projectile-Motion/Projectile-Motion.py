import math 
import os
from ExperimentalData import ExperimentalData
from pathlib import Path
import json

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
#experimentalData = {
#   "gun" = "Vpr-Hunter"
#   "cartridge" = "7.62x51mm"
#   "ammunitionType" = "7.62x51mm FMJ"
#   "velocity" = 840.00
#   "buildingName" = "Miramar Plaza Center"
#   "buildingHeight" = 78.33
#}
myDataSet = [
    ExperimentalData("Vpr-Hunter", "7.62x51mm", "7.62x51mm FMJ", 840.00, "Miramar Plaza Center", 78.33, 9.8),
    ExperimentalData("AK-74", "5.45x39mm", "5.45x39mm PPBS gs", 905.00, "Miramar Plaza Center", 78.33, 9.8),
    ExperimentalData("ADAR 2-15", "5.56x45mm", "5.56x45mm HP", 957.00, "Miramar Plaza Center", 78.33, 9.8),
    ExperimentalData("AS VAL 9x39", "9x39mm", "9x39mm BP gs", 310.00, "Miramar Plaza Center", 78.33, 9.8),
    ExperimentalData("FN GL40", "40x46 mm", "40x46mm M381(HE) grenade", 76.00, "Miramar Plaza Center", 78.33, 9.8)
    ]

calculateProjectileMotion(myDataSet[0])

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "ExperimentalData.json")

with open(myOutputFilePath,"w") as outfile:
    json.dump(myDataSet[0].__dict__, outfile)