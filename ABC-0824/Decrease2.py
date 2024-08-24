# 入力
n = int(input())
a = list(map(int, input().split()))

answer = 0

while True:
    # ソート
    a.sort(reverse=True)
    
    # 条件チェック
    if a[0] == 0 or a[1] == 0:
        break
    
    # 適用
    a[0] -= 1
    a[1] -= 1
    answer += 1

# 出力
print(answer)
