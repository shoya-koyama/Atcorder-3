N = int(input())

result = 0

for i in range(1, 10):
    for j in range(1, 10):
        if (i*j) != N:
            result += (i*j)
            
print(result)

