# 入力
n = int(input())
s = []
c = []

for _ in range(n):
    name, rating = input().split()
    s.append(name)
    c.append(int(rating))

# 文字列の辞書順ソート
s.sort()

# 勝者の番号を求める
sum_rating = sum(c)
winner = sum_rating % n

# 出力
print(s[winner])
