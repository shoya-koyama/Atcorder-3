N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
result = 0
flag = False

for i in range(M):
    result = 0
    for j in range(N):
        result += min(i, A[j])
    if result > M:
        print(i-1)
        flag = True
        break

if flag == False:
    print('infinite')