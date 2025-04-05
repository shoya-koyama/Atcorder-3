N = list(map(int, input().split()))
result = 0

for i in range(N[1]+1):
    result += N[0]**i
    
if result <= 10**9:
    print(result)
else:
    print('inf')