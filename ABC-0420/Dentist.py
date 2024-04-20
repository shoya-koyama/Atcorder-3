# N, Q = list(map(int, input().split()))
# T = list(map(int, input().split()))

# lst = [1] * N
# count = 0

# for i in range(Q):
#     if lst[i-1] == 1:
#         lst[i-1] = 0
#     elif lst[i-1] == 0:
#         lst[i-1] = 1
        
# for s in range(N):
#     if lst[s] == 1:
#         count += 1
        
# print(count)

N, Q = map(int, input().split())
T = list(map(int, input().split()))

lst = [1] * N
count = 0

for i in range(Q):
    index = T[i] - 1  # T[i]の値をインデックスとして使用し、1ベースのインデックスを0ベースに調整
    lst[index] = 1 - lst[index]  # トグル操作: 0なら1に、1なら0に変更

for s in range(N):
    if lst[s] == 1:
        count += 1

print(count)
