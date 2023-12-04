from datetime import datetime
import re
from functools import reduce

puzzleInput = open("inputs/day04.txt", "r").read().split('\n')
start_time = datetime.now()

puzzleLength = len(puzzleInput) -1
pattern = re.compile("\d+")
y = 0
result = 0
while y < len(puzzleInput):
    card = puzzleInput[y].split(": ")[1].split("|")
    hits = set(pattern.findall(card[0])).intersection(pattern.findall(card[1]))
    if hits:
        result += pow(2, len(hits) - 1)
    y+= 1

end_time = datetime.now()

print("1st total is: " + str(result))
print(end_time-start_time)



start_time = datetime.now()
result = 0
pattern = re.compile("\d+")
wonCards = {}
y = 0
while y < len(puzzleInput):
    card = puzzleInput[y].split(": ")[1].split("|")
    hits = set(pattern.findall(card[0])).intersection(pattern.findall(card[1]))
    wonCards[y] = wonCards.get(y, 1)
    if hits:
        for i in range(y + 1, y + len(hits) + 1):
            wonCards[i] = wonCards.get(i, 1) + wonCards[y]
    y+= 1
result = reduce(lambda x,y:x+y, wonCards.values())
end_time = datetime.now()

print("2nd total is: " + str(result))
print(end_time-start_time)