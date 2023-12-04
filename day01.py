from datetime import datetime
stringList = open("inputs/day01.txt", "r").read().split('\n')
start_time = datetime.now()


numberDict = {
    "six": "6",
    "two" : "2",
    "one" : "1",
    "nine": "9",
    "five": "5",
    "four" : "4",
    "three" : "3",
    "eight": "8",
    "seven": "7"
}
result = 0
for word in stringList:
    number = ""
    i = 0
    while number == "":
        if word[i].isnumeric():
            number = word[i]
        else:
            for numberLength in range(3 + i,6 + i):
                if word[i:numberLength] in numberDict:
                    number += numberDict[word[i:numberLength]]
        i += 1
    i = len(word) -1
    while len(number) == 1:
        if word[i].isnumeric():
            number += word[i]
        else:
            for numberLength in range(2,5):
                if word[i - numberLength:i+1] in numberDict:
                    number += numberDict[word[i - numberLength:i+1]]
        i -= 1
    result += int(number)

print("result is: " + str(result))
end_time = datetime.now()