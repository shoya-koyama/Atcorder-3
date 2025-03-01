N = int(input())
A = M = list(map(int, input().split()))

flag = False

for i in range(1, N):
    if A[i-1] >= A[i]:
        flag = True
    
if flag == True:
    print('No')
else:
    print('Yes')