N = list(map(int, input().split()))
X = list(map(int, input().split()))
lst = []
counter = [0] * N[0]

for i in range(N[1]):
    if X[i] == 0:
        min_num = counter.index(min(counter))
        counter[min_num] += 1
        lst.append(min_num + 1)
    else:
        counter[X[i]-1] += 1
        lst.append(X[i])
        
result = ' '.join(map(str, lst))
print(result)