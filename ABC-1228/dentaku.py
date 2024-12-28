def main():
    s = input()
    l = len(s)
    p = 0
    res = 0
    while p < l:
        res += 1
        if p + 1 < l and s[p] == '0' and s[p + 1] == '0':
            p += 2
        else:
            p += 1
    print(res)

if __name__ == "__main__":
    main()


def main():
    s = input()
    l = len(s)
    z = 0
    res = 0

    for nx in s:
        if nx == '0':
            z += 1
        else:
            res += (z + 1) // 2
            z = 0
            res += 1

    res += (z + 1) // 2
    print(res)

if __name__ == "__main__":
    main()
