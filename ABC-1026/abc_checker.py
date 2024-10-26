S = input()
a_l = False
b_l = False
c_l = False

for i in range(len(S)):
    if S[i] == 'A':
        a_l = True
    elif S[i] == 'B':
        b_l = True
    elif S[i] == 'C':
        c_l = True

if (a_l == True) and (b_l == True) and (c_l == True):
    print('Yes')
else:
    print('No')