N = list(map(int, input().split()))
A = list(map(int, input().split()))

count = 0

while True:
    exist = [False] * N[1]  # Mの値（1〜M）に対応する存在確認

    for i in A:
        if 1 <= i <= N[1]:
            exist[i - 1] = True  # 存在する番号をTrueにする

    if False in exist:
        break  # 1〜M に含まれていない値がある → 終了

    A.pop()
    count += 1

print(count)

# N = list(map(int, input().split()))
# A = list(map(int, input().split()))

# count = 0
# flag = False

# while flag == False:
#     for i in range(1, N[1]+1):
#         if i not in A:
#             flag = True
#     A.pop(-1)
#     count += 1
    
# print(count-1)

N = list(map(int, input().split()))
A = list(map(int, input().split()))

count = 0

while True:
    ok = True
    for i in range(1, N[1] + 1):
        if i not in A:
            ok = False
            break
    if not ok:
        break
    A.pop(-1)
    count += 1

print(count)
