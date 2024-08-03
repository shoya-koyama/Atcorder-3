N = int(input())
A = list(map(int, input().split()))

max_num = max(A)

for i in range(N):
    if A[i] == max_num:
        A[i] = -1
        
print(A.index(max(A)) + 1)
