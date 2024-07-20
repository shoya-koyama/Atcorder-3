def TEN(x):
    return 1 if x == 0 else TEN(x - 1) * 10

def main():
    import sys
    input = sys.stdin.read
    N = int(input().strip())
    
    if N == 1:
        print(0)
        return

    N -= 1
    d = 1

    while True:
        x = (d + 1) // 2
        if N <= 9 * TEN(x - 1):
            S = str(TEN(x - 1) + N - 1)
            S = S.ljust(d, ' ')
            for i in range(x, d):
                S = S[:i] + S[d - 1 - i] + S[i + 1:]
            print(S)
            return
        else:
            N -= 9 * TEN(x - 1)
        d += 1

if __name__ == "__main__":
    main()
