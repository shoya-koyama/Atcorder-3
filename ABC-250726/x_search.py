N = list(map(int, input().split()))
S = input()
flg = True

for i in range(N[1]-1, N[2]):
    if S[i] == "x":
        flg = False
        
if flg == True:
    print("Yes")
else:
    print("No")