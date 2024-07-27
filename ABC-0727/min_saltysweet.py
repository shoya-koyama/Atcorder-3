def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    n = data[0]
    x = data[1]
    y = data[2]
    a = data[3:3+n]
    b = data[3+n:3+2*n]
    
    a.sort(reverse=True)
    b.sort(reverse=True)
    
    c1 = 0
    c2 = 0
    sx = 0
    sy = 0
    
    for i in range(n):
        sx += a[i]
        c1 += 1
        if sx > x:
            break
    
    for i in range(n):
        sy += b[i]
        c2 += 1
        if sy > y:
            break
    
    print(min(c1, c2))

if __name__ == "__main__":
    main()
