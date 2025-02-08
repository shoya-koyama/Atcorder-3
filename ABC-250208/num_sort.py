A = list(map(int, input().split()))

A_sort = sorted(A)

if A_sort[0] * A_sort[1] == A_sort[2]:
    print('Yes')
else:
    print('No')