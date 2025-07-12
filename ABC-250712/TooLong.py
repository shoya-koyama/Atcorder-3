N = int(input())
L = [list(map(str, input().split())) for i in range(N)]

result = ''
flag = True
count = 0

for i in range(N):
    if len(L[i][1]) > 3:
        flag = False
        break
    result += L[i][0] * int(L[i][1])
    count += int(L[i][1])
    if count > 100:
        flag = False
        break

if flag == True:
    print(result)
else:
    print('Too Long')