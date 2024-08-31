INF = int(1e18)

def main():
    n = int(input())
    dp0 = 0
    dp1 = -INF

    for _ in range(n):
        x = int(input())
        tmp = dp0
        dp0 = max(dp1 + 2 * x, dp0)
        dp1 = max(tmp + x, dp1)

    print(max(dp0, dp1))

if __name__ == "__main__":
    main()
