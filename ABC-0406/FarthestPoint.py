# import math

# N = int(input())
# M = [list(map(int, input().split())) for i in range(N)]
# tmp = [list() for i in range(N)]
# result = []

# for i in range(N):
#     for s in range(N):
#         tmp[i] = math.sqrt((M[i][0] - M[s][0])**2 + (M[i][1] - M[s][1])**2)
#         result.append(min(tmp[i]))

# print(result)

import math

N = int(input())
M = [list(map(int, input().split())) for i in range(N)]
result = []

for i in range(N):
    max_distance = 0
    max_index = -1
    for s in range(N):
        if i != s:
            distance = math.sqrt((M[i][0] - M[s][0])**2 + (M[i][1] - M[s][1])**2)
            if distance > max_distance:
                max_distance = distance
                max_index = s + 1
    result.append(max_index)

print('\n'.join(map(str, result)))