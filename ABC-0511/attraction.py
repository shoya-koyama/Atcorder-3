N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

atrac = 0

for i in range(1, N):
    if K- A[i-1] < A[i]:
        atrac += 1

print(atrac+1)
        