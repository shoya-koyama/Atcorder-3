def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    S = data[1]

    dp = [0, 0, 0]  # dp[0]: rock, dp[1]: scissors, dp[2]: paper

    for c in S:
        new_dp = [0, 0, 0]
        # 直前に出していなかった手を出すことができる
        new_dp[0] = max(dp[1], dp[2])  # rock
        new_dp[1] = max(dp[0], dp[2])  # scissors
        new_dp[2] = max(dp[0], dp[1])  # paper
        
        # 負ける手を出すことはできない = 勝ち数の最大値を 0 にする
        # 勝つ手を出したら最大値 +1
        if c == 'R':
            new_dp[1] = 0  # scissors
            new_dp[2] += 1  # paper
        elif c == 'S':
            new_dp[2] = 0  # paper
            new_dp[0] += 1  # rock
        elif c == 'P':
            new_dp[0] = 0  # rock
            new_dp[1] += 1  # scissors

        dp = new_dp

    print(max(dp))

if __name__ == "__main__":
    main()
