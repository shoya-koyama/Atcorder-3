# import math

# list = []
# for i in range(3):
#     x,y=input().split()
#     list.append((int(x), int(y)))

# a = math.sqrt(((list[1][0] - list[0][0])**2) + ((list[1][1] - list[0][1])**2))
# b = math.sqrt(((list[2][0] - list[1][0])**2) + ((list[2][1] - list[1][1])**2))
# c = math.sqrt(((list[0][0] - list[2][0])**2) + ((list[0][1] - list[2][1])**2))

# result = []
# result.append(a)
# result.append(b)
# result.append(c)

# max_len = max(result)
# result.remove(max_len)

# if max_len**2 == ((result[0])**2 + (result[1])**2):
#     print('Yes')
# else:
#     print('No')

import math

points = []
for i in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

a = math.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2)
b = math.sqrt((points[2][0] - points[1][0]) ** 2 + (points[2][1] - points[1][1]) ** 2)
c = math.sqrt((points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2)

sides = [a, b, c]
max_len = max(sides)
sides.remove(max_len)

if math.isclose(max_len ** 2, sides[0] ** 2 + sides[1] ** 2):
    print('Yes')
else:
    print('No')
