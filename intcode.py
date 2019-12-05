import csv

class MachineState:
    ADD = 1
    MULT = 2
    IN = 3
    OUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8

    HALT = 99
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1

    def __init__(self, intCodeArray, input):
        self.intCodeArray = intCodeArray
        self.pointer = 0
        self.input = input

    def add(self): # 01
        toAdd1 = self.getParameter(1)
        toAdd2 = self.getParameter(2)
        self.intCodeArray[self.intCodeArray[self.pointer + 3]] = toAdd1 + toAdd2
        self.pointer += 4

    def mult(self): # 02
        toMult1 = self.getParameter(1)
        toMult2 = self.getParameter(2)
        self.intCodeArray[self.intCodeArray[self.pointer + 3]] = toMult1 * toMult2
        self.pointer += 4

    def myInput(self): # 03
        if self.getModeOfParameter(1) == MachineState.POSITION_MODE:
            self.intCodeArray[self.intCodeArray[self.pointer + 1]] = self.input
        elif self.getModeOfParameter(1) == MachineState.IMMEDIATE_MODE:
            self.intCodeArray[self.pointer + 1] = self.input
        else:
            print('Invalid mode on input instruction at position ' + str(self.pointer) + ': ' + str(self.intCodeArray[self.pointer]))
        self.pointer += 2

    def myOutput(self): # 04
        # print('myOutput position: ' + str(self.intCodeArray[self.intCodeArray[self.pointer + 1]]))
        # print('myOutput immediate: ' + str(self.intCodeArray[self.pointer + 1]))
        print('myOutput As Perscribed: ' + str(self.getParameter(1)))
        self.pointer += 2

    def jumpIfTrue(self): # 05
        # Jump if first parameter is not zero
        if self.getParameter(1) != 0:
            self.pointer = self.getParameter(2)
        else:
            self.pointer += 3

    def jumpIfFalse(self): # 06
        # Jump if the first parameter is zero
        if self.getParameter(1) == 0:
            self.pointer = self.getParameter(2)
        else:
            self.pointer += 3

    def lessThan(self): # 07
        # Store 1 at address third if first is less than second, else store 0
        isLessThan = 0
        if self.getParameter(1) < self.getParameter(2):
            isLessThan = 1
        if self.getModeOfParameter(3) == self.POSITION_MODE:
            self.intCodeArray[self.intCodeArray[self.pointer + 3]] = isLessThan
        elif self.getModeOfParameter(3) == self.IMMEDIATE_MODE:
            self.intCodeArray[self.pointer + 3] = isLessThan
        self.pointer += 4

    def equals(self): # 08
        isEqual = 0
        if self.getParameter(1) == self.getParameter(2):
            isEqual = 1
        if self.getModeOfParameter(3) == self.POSITION_MODE:
            self.intCodeArray[self.intCodeArray[self.pointer + 3]] = isEqual
        elif self.getModeOfParameter(3) == self.IMMEDIATE_MODE:
            self.intCodeArray[self.pointer + 3] = isEqual
        self.pointer += 4

    def getParameter(self, parameterNumber): # 09
        modeDigit = 10 * (10**parameterNumber)
        if (self.intCodeArray[self.pointer] // modeDigit) % 10 == self.POSITION_MODE:
            return self.intCodeArray[self.intCodeArray[self.pointer + parameterNumber]]
        elif (self.intCodeArray[self.pointer] // modeDigit) % 10 == self.IMMEDIATE_MODE:
            return self.intCodeArray[self.pointer + parameterNumber]
        return None

    def getModeOfParameter(self, parameterNumber):
        return (self.intCodeArray[self.pointer] // (10 * (10**parameterNumber))) % 10

    OPERATIONS = [
        None, add, mult, myInput, myOutput, jumpIfTrue, jumpIfFalse, lessThan, equals, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
    ]

def runProgram2(ms):
    instruction = ms.intCodeArray[ms.pointer] % 100
    while(instruction != MachineState.HALT):
        if(MachineState.OPERATIONS[instruction] is not None):
            MachineState.OPERATIONS[instruction](ms)
        else:
            print("Invalid op: " + str(instruction) + " at position " + str(ms.pointer))
            print(str(ms.intCodeArray))
            break
        instruction = ms.intCodeArray[ms.pointer] % 100
        

def runProgram(ms):
    instruction = ms.intCodeArray[ms.pointer] % 100
    while(instruction != MachineState.HALT):
        if(instruction == MachineState.ADD):
            ms.add()
        elif(instruction == MachineState.MULT):
            ms.mult()
        elif(instruction == MachineState.IN):
            ms.myInput()
        elif(instruction == MachineState.OUT):
            ms.myOutput()
        elif(instruction == MachineState.JUMP_IF_TRUE):
            ms.jumpIfTrue()
        elif(instruction == MachineState.JUMP_IF_FALSE):
            ms.jumpIfFalse()
        elif(instruction == MachineState.LESS_THAN):
            ms.lessThan()
        elif(instruction == MachineState.EQUALS):
            ms.equals()
        else:
            print("Invalid op: " + str(instruction) + " at position " + str(ms.pointer))
            print(str(ms.intCodeArray))
            break
        instruction = ms.intCodeArray[ms.pointer] % 100



if __name__ == "__main__":
    inputArray = 0 #dummy value
    with open("input05.txt", "r") as fr:
        output = csv.reader(fr) #grab the list of columns in the first (and only) csv row
        for row in output:
            inputArray = row.copy()
    for i in range(len(inputArray)):
        inputArray[i] = int(inputArray[i])
    print("running")
    intCodeArray = inputArray.copy()
    ms = MachineState(intCodeArray, 5)
    runProgram2(ms)
    print("Final state" + str(intCodeArray))