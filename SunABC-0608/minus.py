N, M = list(map(int, input().split()))
H = list(map(int, input().split()))

label = False

for i in range(N):
    M -= H[i]
    if M < 0:
        print(i)
        label = True
        break

if label == False:
    print(N)