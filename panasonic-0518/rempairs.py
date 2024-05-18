def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = []
    b = []
    index = 1
    for i in range(n):
        a.append(int(data[index]))
        b.append(int(data[index + 1]))
        index += 2
    
    dp = [-1] * (1 << n)
    dp[0] = 0
    
    for i in range(1, 1 << n):
        f = False
        for j in range(n):
            for k in range(j + 1, n):
                if ((i >> j) & 1) and ((i >> k) & 1):
                    if (a[j] == a[k] or b[j] == b[k]) and dp[i ^ (1 << j) ^ (1 << k)] == 0:
                        f = True
        dp[i] = f
    
    print("Takahashi" if dp[-1] else "Aoki")

if __name__ == "__main__":
    main()
