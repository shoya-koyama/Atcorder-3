N = list(map(int, input().split()))
T = list(map(int, input().split()))

time = 0
getup = False

for i in range(N[0]):
    time = T[i]
    if i == 0:
        if time <= N[1]:
            getup = True
        else:
            getup = False
            break
    else:
        if time - T[i-1] <= N[1]:
            getup = True
        else:
            getup = False
            break
    
if getup == True:
    print('Yes')
else:
    print('No')