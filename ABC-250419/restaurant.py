Q = int(input())
A = [list(map(int, input().split())) for i in range(Q)]
lst = []
result = []

for i in range(Q):
    if A[i][0] == 1:
        lst.append(A[i][1])
    elif A[i][0] == 2:
        top = lst.pop(0)
        result.append(top)
        
for j in range(len(result)):
    print(result[j])