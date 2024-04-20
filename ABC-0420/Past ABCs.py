import re

# 標準入力から文字列を受け取る
S = input()

# 3桁の数字を抽出するための正規表現パターン
pattern = r'\d{3}'

# 正規表現で数字部分を抽出
match = re.search(pattern, S)

if match:
    number = int(match.group())
    if (1 <= number <= 349) and (number != 316):
        print("Yes")
    else:
        print("No")
