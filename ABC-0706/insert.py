N = list(map(int, input().split()))
B = list(map(int, input().split()))

B.insert(N[1], N[2])

print(" ".join(map(str, B)))