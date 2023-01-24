# Status: Completed
# https://open.kattis.com/problems/nastyhacks
loops = int(input())
for i in range(loops):
    r, e, c = input().split()
    r = int(r)
    e = int(e)
    c = int(c)
    profit = e - c
    if (profit > r):
        result = "advertise"
    if (profit < r):
        result = "do not advertise"
    if (profit == r):
        result = "does not matter"
    print(result)

