N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for i in range(N)]
flag = False

for i in range(N):
    for s in range(M):
        if X[i][s] < A[s]:
            flag = True
        else:
            flag =  False

if flag:
    print('Yes')
else:
    print('No')

#別解

N, M = map(int, input().split())

# 各栄養素の目標量を取得
A = list(map(int, input().split()))

# 各食品から摂取した栄養素量を取得
X = [list(map(int, input().split())) for _ in range(N)]

# 各栄養素の摂取量を合計する
total_nutrients = [sum([X[i][j] for i in range(N)]) for j in range(M)]

# 各栄養素が目標量以上であるかを判定
result = all(total_nutrients[j] >= A[j] for j in range(M))

if result:
    print('Yes')
else:
    print('No')


# N, M = map(int,input().split())
# A = list(map(int,input().split()))
# X = [list(map(int,input().split())) for _ in range(N)]
# for j in range(M):
#   s = 0
#   for i in range(N):
#     s += X[i][j]
#   if s < A[j]:
#     print("No")
#     exit()
# print("Yes")
