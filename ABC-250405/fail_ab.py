N = int(input())
count = 0
cou = 0
result = []

for i in range(1, N+1):
    for j in range(1, N):
        for s in range(1, N):
            if ((2**j * s**2) == i):
                result.append(i)
                count += 1
                
for u in range(len(result)):
    if result[u] == result[u-1]:
        cou += 1
                
print(count-cou)