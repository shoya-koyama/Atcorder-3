N = int(input())
T = input()
A = input()

flag = False

for i in range(N):
    if (T[i] == 'o') and (A[i] == 'o'):
        flag = True
        
if flag == True:
    print('Yes')
else:
    print('No')