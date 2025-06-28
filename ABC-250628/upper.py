S = input()
T = input()
count = 0
al = ''

for i in range(len(S)):
    if S[i].isupper():
        count += 1
        if count == 2:
            al = S[i-1]
            break
        
if (al in T) or (S.islower()):
    print('Yes')
else:
    print('No')
