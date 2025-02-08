N = list(map(int, input().split()))
A = list(map(int, input().split()))

print(N[0]-N[1])

result = []

for i in range(1, N[0]+1):
    if i not in A:
        result.append(i)
        
num = ' '.join(map(str, result))        
print(num)