N = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(2*N-2):
    if (A[i] == A[i+2]) and (A[i+1] != A[i]):
        count += 1
        
print(count)