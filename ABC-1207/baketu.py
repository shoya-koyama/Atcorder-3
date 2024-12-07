N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

volume = 0
now = 0  # 直前の水の追加時刻

for t, v in M:
    # 経過時間分の水量減少
    volume -= (t - now)
    volume = max(volume, 0)  # 水量は負にならない
    volume += v  # 水を追加
    now = t  # 現在時刻を更新

print(volume)


# N = int(input())
# M = [list(map(int, input().split())) for i in range(N)]

# result1 = 0
# result2 = M[0][1]

# for i in range(1, N):
#     result1 += M[i][0] -M[i-1][0]
#     result2 += M[i][1]
    
# print(result2-result1)