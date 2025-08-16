N = int(input())
R = [list(map(int, input().split())) for i in range(N)]

R_lst = []
C_lst = []

for i in range(N):
  R_lst.append(R[i][0])
  
for j in range(N):
  C_lst.append(R[j][1])
  
R_max = max(R_lst)
R_min = min(R_lst)
C_max = max(C_lst)
C_min = min(C_lst)

if (R_max - R_min) >= (C_max - C_min):
  print((R_max - R_min) // 2)
else:
  print((C_max - C_min) // 2)