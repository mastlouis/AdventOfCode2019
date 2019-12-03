import csv
import os

class WireSegment:
    def __init__ (self, distance, direction):
        self.distance = distance
        self.direction = direction

    def distanceUp(self):
        if self.direction == "U":
            return self.distance
        elif self.direction == "D":
            return 0 - self.distance
        else:
            return 0
    def distanceRight(self):
        if self.direction == "R":
            return self.distance
        elif self.direction == "L":
            return 0 - self.distance
        else:
            return 0

class Point:
    def __init__(self, x, y, wire1 = None, wire2 = None, pathSum = None):
        self.x = x
        self.y = y
        self.wire1 = wire1
        self.wire2 = wire2
        self.pathSum = pathSum
    def getManhattan(self):
        return abs(self.x) + abs(self.y)

class WireSegment2:
    def __init__(self, distance, direction, xorigin, yorigin, pathSumFromOrigin = 0):
        self.pathSumFromOrigin = pathSumFromOrigin
        self.direction = direction
        self.left = xorigin
        self.right = xorigin
        self.bottom = yorigin
        self.top = yorigin
        if self.direction == 'U':
            self.top -= distance
        elif self.direction == 'D':
            self.bottom += distance
        elif self.direction == 'L':
            self.left -= distance
        elif self.direction == 'R':
            self.right += distance

    def getOrientation(self):
        if self.direction == 'U' or self.direction == 'D':
            return 'V'
        if self.direction == 'L' or self.direction == 'R':
            return 'H'
    
    def doesIntersect(self, otherSegment):
        if self.right < otherSegment.left:
            return False
        if self.left > otherSegment.right:
            return False
        if self.bottom < otherSegment.top:
            return False
        if self.top > otherSegment.bottom:
            return False
        return True

    def getIntersect(self, otherSegment):
        # If the two segments are parallel
        x = None
        y = None
        if(self.getOrientation() == otherSegment.getOrientation()):
            if(self.getOrientation() == 'H'):
                if(self.left > 0 and otherSegment.left > 0):
                    x = max(self.left, otherSegment.left)
                    y = self.top
                elif(self.right < 0 and otherSegment.right < 0):
                    x = min(self.right, otherSegment.right)
                    y = self.top
                else:
                    x = 0
                    y = self.top
            elif(self.getOrientation() == 'V'):
                if(self.top > 0 and otherSegment.top > 0):
                    x = self.left
                    y = max(self.top, otherSegment.top)
                elif (self.bottom < 0 and otherSegment.bottom < 0):
                    x = self.left
                    y = min(self.bottom, otherSegment.bottom)
                else:
                    x = self.left
                    y = 0
        # If the two segments have opposing orientations
        elif(self.getOrientation() == 'H'):
            x = otherSegment.left
            y = self.top
        elif(self.getOrientation() == 'V'):
            x = self.left
            y = otherSegment.top
        return Point(x, y, self, otherSegment, self.getPathSumOfOrigin(x,y) + otherSegment.getPathSumOfOrigin(x,y))

    def getPathSumOfOrigin(self, x, y):
        if self.direction == 'U':
            return self.pathSumFromOrigin + (self.bottom - y)
        elif self.direction == 'D':
            return self.pathSumFromOrigin + (y - self.top)
        elif self.direction == 'L':
            return self.pathSumFromOrigin + (self.right - x)
        elif self.direction == 'R':
            return self.pathSumFromOrigin + (x - self.left)
        


class Cell:
    def __init__ (self):
        self.wires = []
    
    def addWire(self, name):
        if name not in self.wires:
            self.wires.append(name) 

    def getNumWires(self):
        return len(self.wires)

def greatestVerticalDistance(wire):
    total = 0
    for wireSegment in wire:
        total += wireSegment.distanceUp()
    return total

def greatestHorizontalDistance(wire):
    total = 0
    for wireSegment in wire:
        total += wireSegment.distanceRight()
    return total

def applyWire(grid, wire, name):
    centerX = len(grid[0])
    centerY = len(grid)
    xcoord = centerX
    xcoord = centerY
    i = 0
    for segment in wire:
        i += 1
        if segment.direction == 'U': # 0,0 is in the upper right. I think in pixel coordinates.
            for _ in range(segment.distance):
                ycoord -= 1
                grid[xcoord][ycoord].addWire(name)
        elif segment.direction == 'D':
            for _ in range(segment.distance):
                ycoord += 1
                grid[xcoord][ycoord].addWire(name)
        elif segment.direction == 'L':
            for _ in range(segment.distance):
                xcoord -= 1
                grid[xcoord][ycoord].addWire(name)
        elif segment.direction == 'R':
            for _ in range(segment.distance):
                xcoord += 1
                grid[xcoord][ycoord].addWire(name)
        if grid[xcoord][ycoord].getNumWires() == 2:
            print('intersection at ' + xcoord + ' and ' + ycoord + ' at distance ' + getManhattan(grid, xcoord, ycoord))

def gridToString(grid):
    printString = ""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row == len(grid)//2) and (col == len(grid[0])//2): 
                printString += 'X'
            else:
                printString += str(grid[row][col].getNumWires())
        printString += '\n'
    return printString

def gridToFile(grid, filename = 'output03.txt'):
    with open(filename, 'w' if os.path.isfile(filename) else 'x') as fileWriter:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row == len(grid)//2) and (col == len(grid[0])//2): 
                    fileWriter.write('X')
                else:
                    fileWriter.write(str(grid[row][col].getNumWires()))

def smallestManhattan(grid, numWires = 2):
    acc = len(grid) + len(grid[0])
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if(grid[row][col].getNumWires == numWires) and getManhattan(grid, row, col) < acc:
                acc = row + col
    return acc

def getManhattan(grid, x,y):
    return abs(x - (len(grid)//2)) + abs(y - (len(grid[0])//2))

def main():
    with open("input03.txt", "r") as fr:
        wireStrings = []
        output = csv.reader(fr) 
        for row in output:
            wireStrings.append(row)
    wires = []
    for i in range(len(wireStrings)):
        wires.append([])
        for j in range(len(wireStrings[i])):
            wires[i].append(WireSegment(int(wireStrings[i][j][1:]), wireStrings[i][j][0])) #letter and number
    vertical = 0
    for wire in wires:
        vertical = max(vertical, greatestVerticalDistance(wire))
    horizontal = 0
    for wire in wires:
        horizontal = max(horizontal, greatestHorizontalDistance(wire))
    grid = []
    for row in range ((2 * vertical) + 1):
        grid.append([])
        for _ in range((2 * horizontal) + 1):
            grid[row].append(Cell())
    for i in range (len(wires)):
        applyWire(grid, wire, i)
    gridToFile(grid, 'output03.txt')
    smallestManhattanDistance = smallestManhattan(grid)
    print('Smallest Manhattan Distance: ' + smallestManhattanDistance)

def main2():
    with open("input03.txt", "r") as fr:
        wireStrings = []
        output = csv.reader(fr) 
        for row in output:
            wireStrings.append(row)
    wires = []
    for i in range(len(wireStrings)):
        xstart = 0
        ystart = 0
        wires.append([])
        for j in range(len(wireStrings[i])):
            wires[i].append(WireSegment2(int(wireStrings[i][j][1:]), wireStrings[i][j][0], xstart, ystart))
            if wires[i][j].direction == 'U':
                ystart -= int(wireStrings[i][j][1:])
            elif wires[i][j].direction == 'D':
                ystart += int(wireStrings[i][j][1:])
            elif wires[i][j].direction == 'L':
                xstart -= int(wireStrings[i][j][1:])
            elif wires[i][j].direction == 'R':
                xstart += int(wireStrings[i][j][1:])
    nearest = None
    for wire1segment in wires[0]:
        for wire2segment in wires[1]:
            if wire1segment.doesIntersect(wire2segment):
                if wire1segment.getIntersect(wire2segment).getManhattan() > 0:
                    newIntersect = wire1segment.getIntersect(wire2segment) 
                    if nearest is None:
                        nearest = newIntersect
                    elif newIntersect.getManhattan() < nearest.getManhattan():
                        nearest = newIntersect
    print('Nearest intersection is at (' + str(nearest.x) + ',' + str(nearest.y) + ') with a distance of ' + str(nearest.getManhattan()))

def main3():
    with open("input03.txt", "r") as fr:
        wireStrings = []
        output = csv.reader(fr) 
        for row in output:
            wireStrings.append(row)
    wires = []
    for i in range(len(wireStrings)):
        xstart = 0
        ystart = 0
        pathSum = 0
        wires.append([])
        for j in range(len(wireStrings[i])):
            wires[i].append(WireSegment2(int(wireStrings[i][j][1:]), wireStrings[i][j][0], xstart, ystart, pathSum))
            if wires[i][j].direction == 'U':
                ystart -= int(wireStrings[i][j][1:])
            elif wires[i][j].direction == 'D':
                ystart += int(wireStrings[i][j][1:])
            elif wires[i][j].direction == 'L':
                xstart -= int(wireStrings[i][j][1:])
            elif wires[i][j].direction == 'R':
                xstart += int(wireStrings[i][j][1:])
            pathSum += int(wireStrings[i][j][1:])
    # Now that the sets of wires exist, do stuff with them
    nearest = None
    for wire1segment in wires[0]:
        for wire2segment in wires[1]:
            if wire1segment.doesIntersect(wire2segment):
                if wire1segment.getIntersect(wire2segment).getManhattan() > 0:
                    newIntersect = wire1segment.getIntersect(wire2segment) 
                    if nearest is None:
                        nearest = newIntersect
                    elif newIntersect.getManhattan() < nearest.getManhattan() and newIntersect.pathSum < nearest.pathSum:
                        nearest = newIntersect
    print('Nearest intersection is at (' + str(nearest.x) + ',' + str(nearest.y) + ') with a distance of ' + str(nearest.getManhattan()) + ' and a path sum of ' + str(nearest.pathSum))

if __name__ == "__main__":
    main2()
    main3()