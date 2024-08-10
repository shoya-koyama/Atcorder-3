N = int(input())
S = [input() for i in range(N)]
result = []

for h in range(len(max(S, key=len))-1, -1, -1):
    for j in range(N):
        result.append(S[h][j])
        
print(result)
