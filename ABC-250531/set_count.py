N = int(input())
A = list(map(int, input().split()))

c = set(A)
lst = list(c)
srt = sorted(lst)
result = ' '.join(map(str, srt))

print(len(c))
print(result)