# M = list(map(int, input().split()))
# A = list(range(1, M[0]+1))
# print(A)
# print(A[M[2]-1:M[1]-2:-1])
# A[M[1]-1:M[2]:1] = A[M[2]-1:M[1]-2:-1]
# print(A)

M = list(map(int, input().split()))
A = list(range(1, M[0]+1))

s = M[1] - 1
ed = M[2]

A[s:ed] = A[s:ed][::-1]
print(" ".join(map(str, A)))


# # 入力を受け取る
# N, L, R = map(int, input().split())

# # リストAを生成する
# A = list(range(1, N + 1))

# # LからRまでの範囲を逆順にする
# while L < R:
#     A[L-1], A[R-1] = A[R-1], A[L-1]
#     L += 1
#     R -= 1

# # 結果をスペース区切りで出力する
# print(*A)
