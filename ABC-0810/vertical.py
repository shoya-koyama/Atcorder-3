N = int(input())
S = [input() for i in range(N)]
result = []

for h in range(len(max(S, key=len))-1, -1, -1):
    for j in range(N):
        result.append(S[h][j])
        
print(result)

    
# 模範解答
# N = int(input())
# S = [input() for _ in range(N)]
# M = max(map(len, S))
# T = [["*"] * N for _ in range(M)]
# for i in range(N):
#     for j in range(len(S[i])):
#         T[j][N - i - 1] = S[i][j]
# for i in range(M):
#     while T[i][-1] == "*":
#         T[i].pop()
#     print("".join(T[i]))
