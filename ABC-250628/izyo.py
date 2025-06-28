N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

count = 0

for i in range(N):
    if A[i][0] < A[i][1]:
        count += 1
        
print(count) 