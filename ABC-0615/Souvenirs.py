def main():
    import sys
    input = sys.stdin.read
    from bisect import bisect_left
    from collections import Counter

    data = input().split()
    n = int(data[0])
    m = int(data[1])
    
    a = list(map(int, data[2:n+2]))
    b = list(map(int, data[n+2:n+2+m]))
    
    st = Counter(a)
    ans = 0
    
    for b_i in b:
        keys = sorted(st.keys())
        idx = bisect_left(keys, b_i)
        if idx == len(keys):
            print(-1)
            return
        chosen_key = keys[idx]
        ans += chosen_key
        st[chosen_key] -= 1
        if st[chosen_key] == 0:
            del st[chosen_key]
    
    print(ans)

if __name__ == "__main__":
    main()
