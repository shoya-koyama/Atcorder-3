def main():
    import sys
    input = sys.stdin.read

    data = input().split()
    n, m, k = map(int, data)

    if k < n or k % 2 != n % 2:
        print("No")
        return

    print("Yes")
    path = []
    k -= n

    for i in range(0, n - 1, 2):
        if i != n - 3:
            w = 1 + min(m - 1, k // 2)
            k -= (w - 1) * 2
            for j in range(w):
                path.append((i, m - 1 - j))
            for j in range(w):
                path.append((i + 1, m - w + j))
        elif k <= (m - 1) * 2:
            w = 1 + k // 2
            for j in range(w):
                path.append((i, m - 1 - j))
            for j in range(w):
                path.append((i + 1, m - w + j))
            path.append((i + 2, m - 1))
        else:
            for j in range(m):
                path.append((i, m - 1 - j))
            k -= (m - 1) * 2
            j = 0
            while j < m:
                if k:
                    path.append((i + 1, j))
                    path.append((i + 2, j))
                    path.append((i + 2, j + 1))
                    path.append((i + 1, j + 1))
                    j += 2
                    k -= 2
                else:
                    path.append((i + 1, j))
                    j += 1
            path.append((i + 2, m - 1))

    c = [['|' for _ in range(m - 1)] for _ in range(n)]
    r = [['-' for _ in range(m)] for _ in range(n - 1)]
    
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        if x1 == x2:
            c[x1][min(y1, y2)] = '.'
        else:
            r[min(x1, x2)][y1] = '.'

    print("+" + "+".join(["-"] * m) + "S+")
    for i in range(n):
        print("+" + "".join(['o' + c[i][j] for j in range(m - 1)]) + "o+")
        if i < n - 1:
            print("+" + "+".join(r[i]) + "+")

    print("+" + "+".join(["-"] * m) + "G+")

if __name__ == "__main__":
    main()
