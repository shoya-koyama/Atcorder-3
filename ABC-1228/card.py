# N = list(map(int, input().split()))

# count1 = 1
# count2 = 0

# for i in range(1, len(N)):
#     if N[0] == N[i]:
#         count1 += 1
#     else:
#         count2 += 1

# print(count1)
# if (count1 == 3) or (count2 == 3) or ((count1 == 2) and (count2 == 2)):
#     print('Yes')
# else:
#     print('No')

a = list(map(int, input().split()))
a.sort()

if a[0] == a[1] == a[2] != a[3]:
    print("Yes")
elif a[0] != a[1] == a[2] == a[3]:
    print("Yes")
elif a[0] == a[1] != a[2] == a[3]:
    print("Yes")
else:
    print("No")

def is_full_house(a, b, c, d, e):
    card = [a, b, c, d, e]
    card.sort()
    if (
        card[0] == card[1] == card[2] and
        card[2] != card[3] and
        card[3] == card[4]
    ):
        return True
    if (
        card[0] == card[1] and
        card[1] != card[2] and
        card[2] == card[3] == card[4]
    ):
        return True
    return False

def main():
    a, b, c, d = map(int, input().split())
    for e in range(1, 14):
        if is_full_house(a, b, c, d, e):
            print("Yes")
            return
    print("No")

if __name__ == "__main__":
    main()

