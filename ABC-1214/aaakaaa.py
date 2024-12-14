N = list(map(str, input().split()))
S = input()

result = ''

for i in range(len(S)):
    if S[i] != N[1]:
        result += N[2]
    else:
        result += S[i]
        
print(result)
