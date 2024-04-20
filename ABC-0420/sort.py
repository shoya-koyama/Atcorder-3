def sort_list(A):
    N = len(A)
    operations = []
    made_swap = True
    pass_num = 0
    # パスの回数が N-1 以下で、かつ前のパスで交換が行われた場合のみ続行
    while made_swap and pass_num < N:
        made_swap = False
        for j in range(1, N - pass_num):
            if A[j-1] > A[j]:
                # 隣接する要素を入れ替える
                A[j-1], A[j] = A[j], A[j-1]
                made_swap = True
                operations.append((j, j+1))  # 1ベースのインデックスに変換して記録
        pass_num += 1
    return operations

# 入力の取得
N = int(input())
A = list(map(int, input().split()))

# リストをソートし、操作記録を取得
operations = sort_list(A)

# 操作回数と各操作を出力
print(len(operations))
for op in operations:
    print(op[0], op[1])
