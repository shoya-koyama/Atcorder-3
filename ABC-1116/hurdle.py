# 入力を取得
s = input()

# カウントと結果リストの初期化
c = 0
a = []

# 文字列をループで処理
for i in range(1, len(s)):
    if s[i] == '-':
        c += 1
    else:
        a.append(c)
        c = 0

# リストの要素をスペース区切りで出力
print(" ".join(map(str, a)))

# 入力を取得
# s = input()

# # パイプ記号のインデックスを格納するリスト
# x = []

# # 入力文字列をループしてインデックスを収集
# for i in range(len(s)):
#     if s[i] == '|':
#         x.append(i)

# # 結果を計算し、スペース区切りで出力
# result = []
# for i in range(1, len(x)):
#     result.append(x[i] - x[i - 1] - 1)

# print(" ".join(map(str, result)))
