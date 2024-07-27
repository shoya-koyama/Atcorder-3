H, W = map(int, input().split())
S1, S2 = map(int, input().split())
C = [input().strip() for _ in range(H)]
X = input().strip()

# 現在の位置を0-basedインデックスに変換
si = S1 - 1
sj = S2 - 1

# 操作を処理
for o in X:
    ni, nj = si, sj
    if o == 'L':
        nj -= 1
    elif o == 'R':
        nj += 1
    elif o == 'U':
        ni -= 1
    elif o == 'D':
        ni += 1
    
    # 新しい位置がグリッド内で '.' であれば位置を更新
    if 0 <= ni < H and 0 <= nj < W and C[ni][nj] == '.':
        si, sj = ni, nj

# 結果を1-basedインデックスで出力
print(si + 1, sj + 1)
