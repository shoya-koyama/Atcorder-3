Q = int(input())
query = [list(map(int, input().split())) for i in range(Q)]

result = []

for i in range(Q):
  if query[i][0] == 1:
    result.append(query[i][1])
  elif query[i][0] == 2:
    print(min(result))
    result.remove(min(result))