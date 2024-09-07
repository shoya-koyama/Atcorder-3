n = int(input())  # 数の入力
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())  # 座標の入力

for i in range(n):
    max_dist = 0  # 距離の2乗の最大値
    idx = -1      # 距離が最大になる点の番号(0-indexed)
    for j in range(n):
        dist = (x[i] - x[j])**2 + (y[i] - y[j])**2  # 点i,jの距離の2乗
        if max_dist < dist:
            max_dist = dist
            idx = j
    print(idx + 1)  # 距離が最大になる点の番号(1-indexed)を出力
