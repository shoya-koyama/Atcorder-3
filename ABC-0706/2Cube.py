A = list(map(int, input().split()))
G = list(map(int, input().split()))

if (G[0] < A[3]) and (G[1] < A[4]) and (G[2] < A[5]):
    print('Yes')
else:
    print('No')

# A = list(map(int, input().split()))
# G = list(map(int, input().split()))

# def f(l1, r1, l2, r2):
#   return not (r1 <= l2 or r2 <= l1)

# if f(A[0], A[3], G[0], G[3]) and f(A[1], A[4], G[1], G[4]) and f(A[2], A[5], G[2], G[5]):
#     print('Yes')
# else:
#     print('No')
