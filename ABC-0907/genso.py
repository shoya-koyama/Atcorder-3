N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
# [[3], [2, 4], [3, 1, 2], [2, 1, 2, 4]]
result = 0
for i in range(N):
    if i > result:
        result = A[i][result] - 1
        print(result)
    else:
        result = A[result][i] - 1
        print(result)

print(result + 1)

# n = int(input())
# a = [[0] * n for _ in range(n)]

# for i in range(n):
#     for j in range(i + 1):
#         a[i][j] = int(input()) - 1

# ans = 0
# for i in range(n):
#     if ans >= i:
#         ans = a[ans][i]
#     else:
#         ans = a[i][ans]

# ans += 1
# print(ans)
