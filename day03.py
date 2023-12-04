from datetime import datetime
import re
from functools import reduce

puzzleInput = open("inputs/day03.txt", "r").read().split('\n')
start_time = datetime.now()

class PartNumber:
    def __init__(self, number, xTuple):
        self.number = int(number)
        self.x1      = xTuple[0]
        self.x2      = xTuple[1]-1
        self.minX    = xTuple[0]
        self.maxX    = xTuple[1]
y = 0
result = 0
SYMBOLS = "()`~!@#$%^&*-+=|}{[]:;\"'<>,?/_"
puzzleLength = len(puzzleInput) -1
puzzleWidth = len(puzzleInput[y])- 1
while y < len(puzzleInput):
    partNumbers = [PartNumber(match.group(), match.span()) for match in re.finditer(r"\d+", puzzleInput[y])]
    for partNumber in partNumbers:
        neighBourStrings = ""
        if partNumber.x1 > 0:
            partNumber.minX = partNumber.x1 - 1
            neighBourStrings += puzzleInput[y][partNumber.x1 - 1]
        if partNumber.x2 < puzzleWidth:
            partNumber.maxX = partNumber.x2 + 1
            neighBourStrings += puzzleInput[y][partNumber.x2 + 1]
        if y > 0:
            neighBourStrings += puzzleInput[y - 1][partNumber.minX:partNumber.maxX +1 ]
        if y < puzzleLength:
            neighBourStrings += puzzleInput[y + 1][partNumber.minX:partNumber.maxX +1 ]
        if set(neighBourStrings).intersection(SYMBOLS):
            result += int(partNumber.number)
    y += 1
print("puzzle 1 result is " + str(result))


end_time = datetime.now()
print(end_time-start_time)
puzzleInput = open("inputs/day03.txt", "r").read().split('\n')
start_time = datetime.now()
class PartNumber:
    def __init__(self, number, xTuple):
        self.number = int(number)
        self.x1      = xTuple[0]
        self.x2      = xTuple[1]
        self.minX    = xTuple[0]
        self.maxX    = xTuple[1]
y = 0
result = 0
SYMBOLS = "()`~!@#$%^&*-+=|}{[]:;\"'<>,?/_"
puzzleLength = len(puzzleInput) -1
puzzleWidth = len(puzzleInput[y])- 1
asterixLocation = {}
asterixCounter  = {}
while y < len(puzzleInput):
    partNumbers = [PartNumber(match.group(), match.span()) for match in re.finditer(r"\d+", puzzleInput[y])]
    for partNumber in partNumbers:
        asterixes = []
        if partNumber.x1 > 0:
            partNumber.minX = partNumber.x1 - 1
            if puzzleInput[y][partNumber.x1 - 1] == "*":
                asterixes.append((partNumber.x1 - 1,y))
        if partNumber.x2 < puzzleWidth:
            partNumber.maxX = partNumber.x2 + 1
            if puzzleInput[y][partNumber.x2] == "*":
                asterixes.append((partNumber.x2,y))
        if y > 0:
            k = partNumber.minX
            while k < partNumber.maxX:
                if puzzleInput[y - 1][k] == "*":
                    asterixes.append((k,y-1))
                k += 1
        if y < puzzleLength:
            k = partNumber.minX
            while k < partNumber.maxX:
                if puzzleInput[y + 1][k] == "*":
                    asterixes.append((k,y +1))
                k += 1
        for asterix in asterixes:
            if asterix in asterixLocation:
                asterixLocation[asterix] = asterixLocation[asterix] * partNumber.number
                asterixCounter[asterix] += 1
            else:
                asterixLocation[asterix] = partNumber.number
                asterixCounter[asterix] = 1
    y += 1
total = 0

for key in asterixCounter.keys():
    if asterixCounter[key] == 2:
        total += asterixLocation[key]
end_time = datetime.now()
print("puzzle 2 result: " + str(total))
print(end_time-start_time)
