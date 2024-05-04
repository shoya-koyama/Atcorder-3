M = list(map(int, input().split()))

Label = False

if M[1] < M[2]:
    for i in range(M[1], M[2]+1):
        if i == M[3]:
            Label = True
            break
        else:
            Label = False
else:
    for i in range(M[2], M[1]+1):
        if i == M[3]:
            Label = True
            break
        else:
            Label = False
            
if Label == True:
    print('Yes')
else:
    print('No')


