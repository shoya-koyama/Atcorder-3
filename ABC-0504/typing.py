# S = input()
# T = input()

# results = []
# for i in S:
#     if i in T:
#         result = T.find(i) + 1
#         results.append(result)
#         T = T[T.find(i) + 1:]

# print(' '.join(map(str, results)))

s = input()
t = input()

n = len(s)
m = len(t)
a = [0] * n

j = 0
for i in range(m):
    if j < n and s[j] == t[i]:
        a[j] = i + 1
        j += 1

for i in range(n):
    print(a[i], end=' ' if i < n - 1 else '\n')
