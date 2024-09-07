L, R = list(map(int, input().split()))

if (L == 1) and (R == 0):
    print('Yes')
elif (L == 0) and (R == 1):
    print('No')
elif ((L == 0) and (R == 0)) or ((L == 1) and (R == 1)):
    print('Invalid')
