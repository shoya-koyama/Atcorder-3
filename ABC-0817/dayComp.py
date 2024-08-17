M = list(map(int, input().split()))

if M[1] > M[2]:
    if ((M[1] <= M[0]) and (M[0] <= 24)) or ((0 <= M[0]) and (M[0] <= M[2])):
        print('No')
    else:
        print('Yes')
else:
    if (M[0] >= M[1]) and (M[0] <= M[2]):
        print('No')
    else:
        print('Yes')

