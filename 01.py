import math

def calcFuel(mass):
    return max(math.floor(mass/3)-2, 0)

def calcTotalFuel(mass):
    lastAddedMass = mass
    total = 0
    while (lastAddedMass > 0):
        lastAddedMass = calcFuel(lastAddedMass)
        total += lastAddedMass
    return total

if __name__ == "__main__":
    with open("input01.txt", "r") as fileReader:
        listOfMasses = fileReader.readlines()
    total = 0
    for mass in listOfMasses:
        total += calcTotalFuel(int(mass))
    print("Fuel neeeded for the modules plus fuel: " + str(total))

    # lastAddedMass = total
    # fuelTotal = 0
    # while(lastAddedMass > 0):
    #     print("The " + str(lastAddedMass) + " gallons of fuel needs " + str(calcFuel(lastAddedMass)) + " more gallons of fuel.")
    #     lastAddedMass = calcFuel(lastAddedMass)
    #     fuelTotal += lastAddedMass
    
    # print("Total fuel needed for modules and fuel: " + str(fuelTotal))

    # Too low: 1708313
    # Too high: 5125025