N = list(map(int, input().split()))
A = list(map(int, input().split()))

A_c = A[-N[1]:]
del A[-N[1]:]

result = ' '.join(map(str, A_c + A))
print(result)
