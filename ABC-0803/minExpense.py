N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
result = 0
flag = False

for i in range(M):
    result = 0
    for j in range(N):
        result += min(i, A[j])
    if result > M:
        print(i-1)
        flag = True
        break

if flag == False:
    print('infinite')

# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().split()

#     N = int(data[0])
#     M = int(data[1])
#     A = list(map(int, data[2:2 + N]))

#     s = sum(A)
#     if s <= M:
#         print("infinite")
#         return

#     ok = 0
#     ng = 1000000000

#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         tmp = sum(min(mid, v) for v in A)
#         if tmp <= M:
#             ok = mid
#         else:
#             ng = mid

#     print(ok)

# if __name__ == "__main__":
#     main()
