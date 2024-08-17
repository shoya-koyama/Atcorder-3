def main():
    x = input().strip()

    # 末尾の '0' を削除
    while x.endswith('0'):
        x = x[:-1]

    # もし小数点 '.' が残っていたら、それも削除
    if x.endswith('.'):
        x = x[:-1]

    print(x)

if __name__ == "__main__":
    main()


# def main():
#     x = float(input())
#     print(x)

# if __name__ == "__main__":
#     main()
