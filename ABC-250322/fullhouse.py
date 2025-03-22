# N = list(map(int, input().split()))
# N.sort()

# count1 = 0
# count2 = 0

# lst = []

# for i in range(N):
#     for j in range(N):
#         if N[i] == N[j]:
#             count1 += 1
#             if count1 == 3:
#                 lst.append(N[i])
                
# for s in range(N):
#     for t in range(N):
#         if (N[s] == N[t]) and (N[s] != lst[0]):
#             count2 += 1
            
bk = [0] * 13  # 13個の要素を0で初期化

# 7個の入力を受け取る
for _ in range(7):
    x = int(input())
    bk[x - 1] += 1

# 降順ソート
bk.sort(reverse=True)

# 条件を満たすか判定
if bk[0] >= 3 and bk[1] >= 2:
    print("Yes")
else:
    print("No")
