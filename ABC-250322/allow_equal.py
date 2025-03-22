N = int(input())
result = ''

for i in range(N):
    if N % 2 == 0:
        a = (N // 2)
        if (i == a) or (i == (a-1)):
            result += '='
        else:
            result += '-'
    elif N % 2 == 1:
        b = (N // 2)
        if i == b:
            result += '='
        else:
            result += '-'
            
print(result)

