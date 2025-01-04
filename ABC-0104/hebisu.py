N = list(map(int, input().split()))

count = 0

for i in range(N[0], N[1]+1):
    lst = []
    numStr = str(i)
    for j in range(len(numStr)):
        lst.append(numStr[j])
    lstInt = [int(s) for s in lst]
    if (lstInt[0] == max(lstInt)) and (lstInt.count(max(lstInt)) == 1):
        count += 1
        
print(count)

# def int_pow(a, t):
#     res = 1
#     for _ in range(t):
#         res *= a
#     return res

# def count(r):
#     digit = []
#     while r:
#         digit.append(r % 10)
#         r //= 10
#     digit.reverse()
#     n = len(digit)
#     res = 0

#     for i in range(1, n + 1):
#         if i == n:
#             res += 1
#             break
#         res += int_pow(digit[0], n - 1 - i) * min(digit[0], digit[i])
#         if digit[i] >= digit[0]:
#             break

#     for i in range(n):
#         mx = 9 if i else digit[0] - 1
#         for j in range(1, mx + 1):
#             res += int_pow(j, n - 1 - i)

#     return res

# def main():
#     l, r = map(int, input().split())
#     print(count(r) - count(l - 1))

# if __name__ == "__main__":
#     main()
