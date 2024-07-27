N = int(input())
S = [input() for i in range(N)]
result = False

for i in range(1, N-1):
    if (S[i] == 'sweet') and (S[i-1] == 'sweet'):
        result = True

if result == True:
    print('No')
else:
    print('Yes')