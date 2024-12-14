N = list(map(int, input().split()))
D = [list(map(int, input().split())) for i in range(N[0])]

result = N[1]

for i in range(N[0]):
    if D[i][0] == 1:
        if (result >= 1600) and (result <= 2799):
            result += D[i][1]
        else:
            result += 0
    elif D[i][0] == 2:
        if (result >= 1200) and (result <= 2399):
            result += D[i][1]
        else:
            result += 0

print(result)