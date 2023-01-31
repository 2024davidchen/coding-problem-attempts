# Status: Complete
# https://open.kattis.com/problems/detaileddifferences
loops = int(input())
for a in range(loops):
    string1 = input()
    string2 = input()
    result = ""
    for i in range(len(string1)):
        if (string1[i] == string2[i]):
            result += "."
        else:
            result += "*"
    print(string1)
    print(string2)
    print(result)