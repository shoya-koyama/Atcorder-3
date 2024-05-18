class Card:
    def __init__(self, a, c, index):
        self.a = a
        self.c = c
        self.index = index

# 入力
n = int(input())
cards = []
for i in range(n):
    a, c = map(int, input().split())
    cards.append(Card(a, c, i))

# C[i] の昇順にソート
cards.sort(key=lambda card: card.c)

# 答えを求める計算
ans = []
v = 0
for card in cards:
    if card.a > v:
        v = card.a
        ans.append(card.index)

ans.sort()

# 出力
m = len(ans)
print(m)
print(' '.join(str(i + 1) for i in ans))
