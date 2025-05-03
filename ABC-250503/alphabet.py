import random

s = input()
al = 'abcdefghijklmnopqrstuvwxyz'

result = []

for i in range(len(al)):
    for j in range(len(s)):
        if al[i] not in s:
            result.append(al[i])

print(random.choice(result))

# s = input()
# al = 'abcdefghijklmnopqrstuvwxyz'

# for i in range(len(al)):
#     for j in range(len(s)):
#         if al[i] == s[j]:
#             al.replace(al[i], '?')
        
# print(al)
