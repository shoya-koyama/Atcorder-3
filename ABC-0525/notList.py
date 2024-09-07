A, B = list(map(int, input().split()))

lst = [1, 2, 3]

if A == B:
    print(-1)

else:
    result = [i for i in lst if i != A and i != B]
    print(*result)