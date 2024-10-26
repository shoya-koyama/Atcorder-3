S = [input() for _ in range(8)]
result = set()

for i in range(8):
    for j in range(8):
        if S[i][j] == '#':
            result.add(i)
            result.add(j)

result_a = len(result)
print((result_a - 2) ** 2)

# def check_square(board, i, j):
#     # 同じ行にすでにコマがあるか確認
#     for k in range(8):
#         if board[i][k]:
#             return False
#     # 同じ列にすでにコマがあるか確認
#     for k in range(8):
#         if board[k][j]:
#             return False
#     return True

# # 盤面入力
# board = []
# for _ in range(8):
#     row = input()
#     board.append([c == '#' for c in row])

# ans = 0

# # それぞれのマスについてコマが置けるか判定
# for i in range(8):
#     for j in range(8):
#         if check_square(board, i, j):
#             ans += 1

# print(ans)


# # 各行・各列にコマがあるか
# # はじめはすべて False にしておく
# row = [False] * 8
# column = [False] * 8

# # 8x8の盤面を入力
# for i in range(8):
#     line = input().strip()  # 各行を入力
#     for j in range(8):
#         # コマが置かれていたら
#         if line[j] == '#':
#             # 対応する行と列を True に
#             row[i] = True
#             column[j] = True

# # False の行数 × False の列数 が答え
# result = row.count(False) * column.count(False)
# print(result)
