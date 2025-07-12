N = list(map(int, input().split()))
L = [list(map(int, input().split())) for i in range(N[0])]

count = 0

for i in range(N[0]):
    if (L[i][0] <= N[1]) and (L[i][1] >= N[2]):
        count += 1
        
print(count)