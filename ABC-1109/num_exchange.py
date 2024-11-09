N = int(input())

M = str(N)

result1 = ''
result2 = ''

a, b, c = M[0], M[1], M[2]

result1 = b + c + a
result2 = c + a + b
print(f"{result1} {result2}")

