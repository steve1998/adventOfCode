import math

# Functions
def calculateMassforModule(mass):
    result = math.floor((mass / 3)) - 2
    return result

# main
filepath = 'day1input.txt'
input = []
result = 0

with open(filepath, 'r') as fp: 
    line = fp.readline()
    line = line.rstrip('\n')
    input.append(int(line))

    while line:    
        line = fp.readline()
        if line != '':
            line = line.rstrip('\n')
            input.append(int(line))

for i in input:
    result += calculateMassforModule(i)

print(result)

