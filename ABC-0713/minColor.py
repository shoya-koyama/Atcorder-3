L = list(map(int, input().split()))
C = input()

if C == 'Red':
    L.pop(0)
    print(min(L))
    
elif C == 'Green':
    L.pop(1)
    print(min(L))
    
elif C == 'Blue':
    L.pop(2)
    print(min(L))
