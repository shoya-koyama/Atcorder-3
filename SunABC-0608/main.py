def main():
    n = int(input())
    l = 1
    a = [['' for _ in range(730)] for _ in range(729)]

    a[0][0] = '#'
    
    for k in range(n):
        for x in range(3):
            for y in range(3):
                if x == 0 and y == 0:
                    continue
                elif x == 1 and y == 1:
                    for i in range(l):
                        for j in range(l):
                            a[x * l + i][y * l + j] = '.'
                else:
                    for i in range(l):
                        for j in range(l):
                            a[x * l + i][y * l + j] = a[i][j]
        l *= 3

    for i in range(l):
        print(''.join(a[i][:l]))

if __name__ == "__main__":
    main()
