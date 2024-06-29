N = int(input())
S = input()
count = 1

for i in range(2, N-1):
    if ((S[i-2] == 'A') and (S[i-1] == 'B') and (S[i] == 'A')):
        S = S.replace(S[i-1], "").replace(S[i], "")
        count += 1
    elif ((S[i-2] == 'B') and (S[i-1] == 'A') and (S[i] == 'B')):
        S = S.replace(S[i-1], "").replace(S[i], "")
        count += 1

print((count) % (10**9 + 7))
