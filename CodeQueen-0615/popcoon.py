import itertools

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    
    ans = n
    for bit in range(1 << n):
        exist = [False] * m
        cnt = 0
        for i in range(n):
            if bit & (1 << i):
                cnt += 1
                for j in range(m):
                    if s[i][j] == 'o':
                        exist[j] = True
        all_exist = all(exist)
        if all_exist:
            ans = min(ans, cnt)
    
    print(ans)

if __name__ == "__main__":
    main()
