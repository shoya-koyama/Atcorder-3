N = list(map(int, input().split()))
result = []

for i in range(N[0]+1):
    if i < N[1]:
        result.append(1)
    else:
        result.append(N[i-N[1]] + N[i-N[1]+1])
        
print(sum(result) % 10**9)
