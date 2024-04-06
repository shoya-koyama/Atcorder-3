N = int(input())
result = ''

for i in range(N):
    if (i+1) % 3 == 0:
        result += 'x'
    else:
        result += 'o'
        
print(result)