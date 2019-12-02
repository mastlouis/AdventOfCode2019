ADD = 1
MULT = 2
HALT = 99

import csv

def runProgram(opCodeArray):
    pointer = 0
    while(opCodeArray[pointer] != HALT):
        if(opCodeArray[pointer] == ADD):
            opCodeArray[opCodeArray[pointer + 3]] = opCodeArray[opCodeArray[pointer + 1]] + opCodeArray[opCodeArray[pointer + 2]]
        elif(opCodeArray[pointer] == MULT):
            opCodeArray[opCodeArray[pointer + 3]] = opCodeArray[opCodeArray[pointer + 1]] * opCodeArray[opCodeArray[pointer + 2]]
        else:
            print("Invalid op: " + str(opCodeArray[pointer]) + " at position " + str(pointer))
            print(str(opCodeArray))
            break
        pointer += 4

def findParameters(inputArray, targetOutput):
    for i in range(99):
        for j in range(99):
            freshInput = inputArray.copy()
            freshInput[1] = i
            freshInput[2] = j
            runProgram(freshInput)
            if(freshInput[0] == targetOutput):
                return (i,j)
    return (-1, -1)


if __name__ == "__main__":
    targetOutput = 19690720

    inputArray = 0 #dummy value
    with open("input02.txt", "r") as fr:
        output = csv.reader(fr) #grab the list of columns in the first (and only) csv row
        for row in output:
            inputArray = row.copy()
    for i in range(len(inputArray)):
        inputArray[i] = int(inputArray[i])
    opCodeArray = inputArray.copy()
    #set the machine state   
    opCodeArray[1] = 12
    opCodeArray[2] = 2

    runProgram(opCodeArray)
    print("Output at potition zero: " + str(opCodeArray[0]))
    print("Final State: " + str(opCodeArray))

    print("The noun and verb that produce " + str(targetOutput) + " are " + str(findParameters(inputArray, targetOutput)))

