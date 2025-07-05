N = list(map(int, input().split()))
A = list(map(int, input().split()))

if sum(A) <= N[1]:
    print("Yes")
else:
    print("No")