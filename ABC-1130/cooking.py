n, d = map(int, input().split())
s = input()
b = 0
for c in s:
    if c == '.':
        b += 1
print(b + d)
