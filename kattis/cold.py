# Status: Complete
# https://open.kattis.com/problems/cold
loops = int(input())
counter = 0

# Takes all the input temperatures
inputLine = input().split()

# Makes all values in list into ints
for i in range(len(inputLine)):
    inputLine[i] = int(inputLine[i])
    if inputLine[i] < 0:
        counter += 1
print(counter)
