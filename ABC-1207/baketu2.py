h, w, d = map(int, input().split())
s = [input().strip() for _ in range(h)]

ans = 0

for i1 in range(h):
    for j1 in range(w):
        if s[i1][j1] == '#':
            continue  # 床のマスではない
        for i2 in range(h):
            for j2 in range(w):
                if s[i2][j2] == '#' or (i1 == i2 and j1 == j2):
                    continue  # 床のマスではないか片方の加湿器と同じ場所
                tmp = 0
                for i in range(h):
                    for j in range(w):
                        if s[i][j] == '.' and (
                            abs(i - i1) + abs(j - j1) <= d or abs(i - i2) + abs(j - j2) <= d
                        ):
                            tmp += 1  # 加湿されている
                ans = max(ans, tmp)

print(ans)
