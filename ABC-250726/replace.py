S = input()

re_S = S.replace(".", "o")

for i in range(len(re_S)):
    if re_S[i] == "o":
        if re_S[i-1] == "o":
            re_S.replace(re_S[i-1], ".")
            
print(re_S)

# S = input()
# re_S = S.replace(".", "o")

# # 文字列をリストに変換（変更可能にするため）
# lst = list(re_S)

# for i in range(1, len(lst)):
#     if lst[i] == "o" and lst[i-1] == "o":
#         lst[i] = "."  # 2つ目の o を . に置換

# # リストを文字列に戻す
# re_S = "".join(lst)
# print(re_S)