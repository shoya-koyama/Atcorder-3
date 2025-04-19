n, m = map(int, input().split())

a = [[] for _ in range(m)]
idx = [[] for _ in range(n)]
cnt = [0] * m

# 各要素の初期値をカウント
for i in range(m):
    k, *rest = map(int, input().split())
    if len(rest) < k:
        rest += list(map(int, input().split()))
    cnt[i] = k
    a[i] = [x - 1 for x in rest]
    for e in a[i]:
        idx[e].append(i)

ans = 0
# 各要素の初期値をカウント
for _ in range(n):
    b = int(input()) - 1
    for id in idx[b]:
        cnt[id] -= 1
        if cnt[id] == 0:
            ans += 1
    print(ans)
