S = input()

result = ''

for i in range(len(S)):
    if S[i].isupper():
        result += S[i]
        
print(result)