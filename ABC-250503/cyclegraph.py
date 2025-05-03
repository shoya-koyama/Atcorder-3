N,M = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(M)]

lst = [0] * N

for i in range(M):
    lst[A[i][0]-1] += 1
    lst[A[i][1]-1] += 1
    
flag = False
for j in range(len(lst)):
    if lst[j] != 2:
        flag = True
    
if flag == False:
    print('Yes')
else:
    print('No')