# Status:
# https://open.kattis.com/problems/r2
numList = input().split()
r1 = int(numList[0])
s = int(numList[1])
r2 = s + (s - r1)
print(r2)