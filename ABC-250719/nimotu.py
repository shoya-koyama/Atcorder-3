s = input()
count = 0
lst = ""
result = []

for i in range(len(s)):
    if s[i] == "#":
        lst += str(i + 1) + ","
        count += 1
        if count == 2:
            result.append(lst.rstrip(","))
            lst = ""
            count = 0

print(result)

# 以下はミス
s = input()
count = 0
lst = ""
result = []

for i in range(len(s)):
    if count != 2:
        if s[i] == "#":
            lst += str(i+1)
            lst += ","
            count += 1
        else:
            pass
    else:
        # ＃の後、余計な1文字処理をしたあとでしか保存されない。
        # つまり最後のペアが記録されない。
        result.append(lst)
        lst = ""
        count = 0
        
print(result)