N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(N):
        if (j-i) == (A[i] + A[j]):
            count += 1

print(count)

# from collections import Counter

# N = int(input())
# A = list(map(int, input().split()))

# # i + A[i] のカウントを記録
# left_counter = Counter()
# for i in range(N):
#     left_counter[i + A[i]] += 1

# # j - A[j] と一致する個数を集計
# count = 0
# for j in range(N):
#     key = j - A[j]
#     count += left_counter[key]

# print(count)
