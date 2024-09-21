S = input()

result = ''
for i in range(len(S)):
    if S[i] != '.':
        result += S[i]
        
print(result)
