import sys
import bisect

inf = 1 << 30  # inf > 10^9

def calc_lis(x):
    n = len(x)
    dp = [inf] * n
    ret = [0] * n
    for i in range(n):
        pos = bisect.bisect_left(dp, x[i])
        dp[pos] = x[i]
        ret[i] = pos + 1
    return ret

def solve():
    # 入力
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    # l_lis[i] : 最後の要素が a[i] である条件下の LIS の長さ
    # r_lis[i] : 最初の要素が a[i] である条件下の LIS の長さ
    l_lis = calc_lis(a)
    a.reverse()
    a = [inf - e for e in a]
    r_lis = calc_lis(a)
    a.reverse()
    a = [inf - e for e in a]
    r_lis.reverse()

    L = max(l_lis)
    ans = [i for i in range(n) if l_lis[i] + r_lis[i] - 1 == L]

    # 出力
    print(len(ans))
    print(' '.join(str(i + 1) for i in ans))

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    for _ in range(T):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        solve_case(a)

def solve_case(a):
    n = len(a)

    # l_lis[i] : 最後の要素が a[i] である条件下の LIS の長さ
    # r_lis[i] : 最初の要素が a[i] である条件下の LIS の長さ
    l_lis = calc_lis(a)
    a.reverse()
    a = [inf - e for e in a]
    r_lis = calc_lis(a)
    a.reverse()
    a = [inf - e for e in a]
    r_lis.reverse()

    L = max(l_lis)
    ans = [i for i in range(n) if l_lis[i] + r_lis[i] - 1 == L]

    # 出力
    print(len(ans))
    print(' '.join(str(i + 1) for i in ans))

if __name__ == "__main__":
    main()
