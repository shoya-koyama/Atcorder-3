N = int(input())
A = list(map(int, input().split()))
lst = []

for i in range(N+1):
    count = 0
    for j in range(N):
        if A[j] >= i:
            count += 1
    lst.append(count)
    
max_i = [i for i, val in enumerate(lst) if i <= val]
print(max(max_i))