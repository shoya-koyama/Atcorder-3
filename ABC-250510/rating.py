M = list(map(int, input().split()))

if M[1] == 1:
    if (M[0] >= 1600) and (M[0] <= 2999):
        print('Yes')
    else:
        print('No')
elif M[1] == 2:
    if (M[0] >= 1200) and (M[0] <= 2399):
        print('Yes')
    else:
        print('No')

