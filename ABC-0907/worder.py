def main():
    s = input().strip()
    t = input().strip()
    ans = []
    n = len(s)
    
    while s != t:
        nxt = 'z' * n
        for i in range(n):
            if s[i] != t[i]:
                tmp = list(s)
                tmp[i] = t[i]
                tmp_str = ''.join(tmp)
                nxt = min(nxt, tmp_str)
        ans.append(nxt)
        s = nxt
    
    sz = len(ans)
    print(sz)
    for e in ans:
        print(e)

main()

# -----------------------------------

def main():
    s = list(input().strip())
    t = list(input().strip())
    ans = []
    v = []
    n = len(s)
    
    # s[i] が t[i] より大きい場合
    for i in range(n):
        if s[i] > t[i]:
            v.append(i)
    
    # s[i] が t[i] より小さい場合
    for i in range(n - 1, -1, -1):
        if s[i] < t[i]:
            v.append(i)
    
    sz = len(v)
    
    # s の指定した位置を t の文字に置き換え、結果を ans に追加
    for i in range(sz):
        s[v[i]] = t[v[i]]
        ans.append(''.join(s))
    
    # 結果の出力
    print(sz)
    for e in ans:
        print(e)

main()
