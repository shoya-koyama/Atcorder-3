# N = int(input())
# P = list(map(int, input().split()))
# r = 1
# lst = [0] * N

# for u in range(N):
#     for i in range(N):
#         count = 0
#         a = max(P)
#         if P[i] == a:
#             lst[i] = r
#             count += 1
#         r += count
#         P[i] = -1

# print(lst)

N = int(input())
P = list(map(int, input().split()))

# (値, インデックス) のタプルを作成し、値を降順にソート
sorted_P = sorted(enumerate(P), key=lambda x: -x[1])

lst = [0] * N
r = 1  # 現在のランク
prev_value = None  # 直前の値
count = 0  # 同順位の個数

for i, (index, value) in enumerate(sorted_P):
    if value != prev_value:
        r += count  # ランクを更新
        count = 1  # カウントをリセット
    else:
        count += 1  # 同じ値ならカウントを増やす
    
    lst[index] = r
    prev_value = value  # 直前の値を更新

print(lst)
# これは、与えられた整数のリストに対して、各整数の順位を求めるプログラムです。