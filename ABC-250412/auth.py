N = int(input())
S = [input() for i in range(N)]

count = 0
auth = False

for i in range(N):
    if S[i] == 'login':
        auth = True
    elif S[i] == 'logout':
        auth = False
    if (auth == False) and (S[i] == 'private'):
        count += 1

print(count)