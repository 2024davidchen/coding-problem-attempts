# Status: Complete
# https://open.kattis.com/problems/sumkindofproblem
loops = int(input())

for k in range(loops):
    inputList = input().split()
    index = inputList[0]
    num = int(inputList[1])
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(1, 1 + num):
        sum1 += i
        sum2 += (i * 2) - 1
        sum3 += i * 2
    print(str(index) + " " + str(sum1) + " " + str(sum2) + " " + str(sum3))