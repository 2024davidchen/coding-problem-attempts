# Status: In Progress
# https://open.kattis.com/problems/aboveaverage
totalLoops = int(input())
for repeats in range(totalLoops):
    line = input().split()
    numOfGrades = int(line[0])
    total = 0.0
    for i in range(1, numOfGrades + 1):
        total += int(line[i])
    average = total / numOfGrades
    aboveAverage = 0
    for i in range(1, numOfGrades + 1):
        if (int(line[i]) > average):
            aboveAverage += 1
    avgStr = str(round(aboveAverage  * 100 / numOfGrades, 3))
    while (len(avgStr) < 6):
        avgStr += "0"
    print(avgStr + "%")