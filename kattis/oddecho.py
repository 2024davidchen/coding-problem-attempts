# Status: Complete
# https://open.kattis.com/problems/oddecho

odd = True
numOfLines = int(input())

# Repeat numOfLines times to get through all the rest of the input
for i in range(numOfLines):
    currentLine = input()
    if (odd):
        print(currentLine)
# Toggles odd
    odd = not odd