mass = [
    [2, 1, 0, 1],
    [1, 2, 1, 0]
]
# mass[i][j] : 長方形 [[j, j + 1], [i, i + 1]] の面積 x 2

inf = 4000000000

# 入力
a, b, c, d = map(int, input().split())

# 計算
ans = 0
for fy in range(2):
    for fx in range(4):
        x1 = (a - fx + 3 + inf) // 4
        x2 = (c - fx + 3 + inf) // 4
        count_x = x2 - x1  # x 方向の個数
        y1 = (b - fy + 1 + inf) // 2
        y2 = (d - fy + 1 + inf) // 2
        count_y = y2 - y1  # y 方向の個数
        ans += count_x * count_y * mass[fy][fx]

# 出力
print(ans)
