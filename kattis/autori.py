# Status: Complete
# https://open.kattis.com/problems/autori
fullName = input().split('-')
initials = ''
for name in fullName:
    initials += name[0]
print(initials)