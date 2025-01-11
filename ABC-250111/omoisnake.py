n, d = map(int, input().split())
t = []
l = []

# 入力を受け取る
for _ in range(n):
    ti, li = map(int, input().split())
    t.append(ti)
    l.append(li)

# 各 k (1 から d まで) について計算
for k in range(1, d + 1):
    ans = 0
    for i in range(n):
        ans = max(ans, t[i] * (l[i] + k))
    print(ans)
