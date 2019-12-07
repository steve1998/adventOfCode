import math

# Functions
def calculateMassforModule(mass):
    result = math.floor((mass / 3)) - 2
    return result

def calculateMassforModuleWhile(mass):
    result = 0
    divResult = math.floor((mass / 3)) - 2

    while divResult > 0:
        divResult = math.floor((divResult / 3)) - 2
        result += divResult

    return result

def readFile():
    input = []
    filepath = 'day1input.txt'

    with open(filepath, 'r') as fp: 
        line = fp.readline()
        line = line.rstrip('\n')
        input.append(int(line))

        while line:    
            line = fp.readline()
            if line != '':
                line = line.rstrip('\n')
                input.append(int(line))

    return input

# Main
def main():
    # Data
    input = []
    result = 0
    
    input = readFile()

    # Part 1
    for i in input:
        result += calculateMassforModule(i)

    print(result)

    # Part 2
    for i in input:
        result += calculateMassforModuleWhile(i)

    print(result)

main()