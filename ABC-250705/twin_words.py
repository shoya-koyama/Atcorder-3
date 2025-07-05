N = int(input())
S = [list(map(str, input().split())) for i in range(N)]
lst = []

for i in range(N):
    for j in range(N):
        if i != j:
            twin = S[i] + S[j]
            twinWord = ''.join(twin)
            if twinWord not in lst:
                lst.append(twinWord)
            
print(len(lst))