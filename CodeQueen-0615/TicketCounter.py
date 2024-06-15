N, A = list(map(int, input().split()))
T = list(map(int, input().split()))
result = []
result.append(T[0] + A)

for i in range(1, N):
    tmp = T[i]
    if tmp <= result[i-1]:
        tmp = result[i-1]
    result.append(tmp + A)
    
print(*result, sep='\n')