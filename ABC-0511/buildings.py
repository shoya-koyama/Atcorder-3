N = int(input())
H = list(map(int, input().split()))

param = False

for i in range(N):
    if H[i] > H[0]:
        param = True
        print(i+1)
        break

if param == False:
    print(-1)
