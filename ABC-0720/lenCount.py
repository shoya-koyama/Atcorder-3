N = list(map(int, input().split()))
L = list(map(int, input().split()))

result = 0

while len([n for n in L if n >= N[1]]) < N[2]:
    for i in range(N[0]):
        L[i] += 1
    result += 1

print(result)