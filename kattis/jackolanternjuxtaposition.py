# Status: Complete
# https://open.kattis.com/problems/jackolanternjuxtaposition
numList = input().split()
product = 1
for i in numList:
    product *= int(i)
print(str(product))