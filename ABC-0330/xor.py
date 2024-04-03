def main():
    a, b, C = map(int, input().split())
    c = bin(C).count('1')  # popcountの代わりにビットカウント

    if (a + b + c) % 2 != 0 or a + b + c > 120 or a > b + c or b > c + a or c > a + b:
        print("-1")
        return

    n00 = 60 - (a + b + c) // 2
    n01 = (-a + b + c) // 2
    n10 = (a - b + c) // 2
    n11 = (a + b - c) // 2

    X = Y = 0
    for B in range(59, -1, -1):  # 60ビットを上から見る
        X *= 2
        Y *= 2
        if 1 & (C >> B):  # CのBビット目が1の場合
            if n10:
                X += 1  # XのBビット目を1に、YのBビット目を0に
                n10 -= 1
            else:
                Y += 1
                n01 -= 1
        else:  # CのBビット目が0の場合
            if n00:
                n00 -= 1  # どちらも0にし、在庫を減らす
            else:
                X += 1
                Y += 1
                n11 -= 1

    print(X, Y)

if __name__ == '__main__':
    main()
