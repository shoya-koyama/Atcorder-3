def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:]))

    a.sort()
    res = int(2e9)
    
    for i in range(k + 1):
        res = min(res, a[i + (n - k) - 1] - a[i])
    
    print(res)

if __name__ == "__main__":
    main()
