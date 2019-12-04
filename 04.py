def getNumPasswords(min, max):
    numValidPasswords = 0
    for i in range(min, max):
        if isAscendingOnly(i) and containsDouble(i):
            numValidPasswords += 1
    return numValidPasswords

def getNumPasswords2(min, max):
    numValidPasswords = 0
    for i in range(min, max):
        if isAscendingOnly(i) and containsOneExactDouble(i):
            numValidPasswords += 1
    return numValidPasswords

def isAscendingOnly(num):
    while(num > 0):
        if num % 10 < (num // 10) % 10:
            return False
        num //= 10
    return True

def containsDouble(num):
    while(num > 0):
        if num % 10 == (num // 10) % 10:
            return True
        num //= 10
    return False

def containsOneExactDouble(num):
    if num % 10 == (num // 10) % 10 and num % 10 != (num // 100) % 10:
        return True
    exclusionNumber = num % 10
    num //= 10
    while(num > 0):
        if num % 10 == (num // 10) % 10 and num % 10 != (num//100) % 10 and num % 10 != exclusionNumber:
            return True
        exclusionNumber = num % 10
        num //= 10
    return False

def main():
    print(getNumPasswords(171309,643603))
    print(getNumPasswords2(171309,643603))
    

if __name__ == "__main__":
    main()