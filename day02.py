from functools import reduce
from datetime import datetime


puzzleInput = open("inputs/day02.txt", "r").read().split('\n')

start_time = datetime.now()
colours = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
total = 0
for i in range(0,len(puzzleInput)):
    badGame = False
    balls = puzzleInput[i].split(": ")[1].replace(";", ",").split(", ")
    k=0
    while k < len(balls) and badGame == False:
        ball = balls[k].split(" ")
        if int(ball[0]) > colours[ball[1]]:
            badGame = True
        k += 1
    if not badGame:
        total += i + 1

end_time = datetime.now()
print(end_time-start_time)
print("puzzle 1 total = " + str(total))

start_time = datetime.now()
total = 0
for i in range(0,len(puzzleInput)):
    colours = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    } 
    for round in puzzleInput[i].split(": ")[1].split("; "):
        for ball in round.split(", "):
            if int(ball.split(" ")[0]) > colours[ball.split(" ")[1]]:
                colours[ball.split(" ")[1]] = int(ball.split(" ")[0])
    total += reduce(lambda x,y: x*y, colours.values())
end_time = datetime.now()
print(end_time-start_time)
print("Puzzle 2 total: " + str(total))