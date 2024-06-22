N = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(2*N-2):
    if (A[i] == A[i+2]) and (A[i+1] != A[i]):
        count += 1
        
print(count)

#別解

def main():
    # 標準入力から整数値nを読み取る
    n = int(input())
    
    # 標準入力からn*2個の整数を読み取り、リストaに格納する
    a = list(map(int, input().split()))
    
    # 結果を格納する変数resを初期化する
    res = 0
    
    # aの要素をチェックし、a[i]がa[i + 2]と等しい場合、resを増加させる
    for i in range(n * 2 - 2):
        if a[i] == a[i + 2]:
            res += 1
    
    # 結果を出力する
    print(res)

if __name__ == "__main__":
    main()
