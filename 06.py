
class Orbit:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def setParent(self, parent):
        self.parent = parent

    def getOrbitSum(self):
        if self.parent is None:
            return 0
        return 1 + self.parent.getOrbitSum()

def filterFunction(element, target = 'RMS'):
    return element.name == target

def orbitsToList(inputs):
    orbitList = []
    for item in inputs:
        satteliteNames = item.split(")")
        parent = None
        child = None
        for i in range(len(orbitList)):
            if orbitList[i].name == satteliteNames[0]:
                parent = orbitList[i]
            if orbitList[i].name == satteliteNames[1]:
                child = orbitList[i]
        if child is None and parent is None:
            parent = Orbit(satteliteNames[0])
            child = Orbit(satteliteNames[1], parent)
            parent.addChild(child)
            orbitList.append(child)
            orbitList.append(parent)
        elif child is None: # parent must already exist
            child = Orbit(satteliteNames[1], parent)
            parent.addChild(child)
            orbitList.append(child)
        elif parent is None: # child must already exist
            parent = Orbit(satteliteNames[0])
            parent.addChild(child)
            child.setParent(parent)
            orbitList.append(parent)
        else: #both must already exist
            parent.addChild(child)
            child.setParent(parent)
    return orbitList

def countOrbits(orbitTreeList):
    sum = 0
    for orbitTree in orbitTreeList:
        sum += orbitTree.getOrbitSum()
    return sum

def part1():
    with open("input06.txt", "r") as fileReader:
        inputs = [item for item in fileReader.read().rstrip().split("\n")]
    print(str(inputs))
    orbitTreeList = orbitsToList(inputs)
    print('Sum is ' + str(countOrbits(orbitTreeList)))
    # Wrong guesses
    # 6509

if __name__ == "__main__":
    part1()