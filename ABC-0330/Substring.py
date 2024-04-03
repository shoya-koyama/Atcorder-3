S = input()

def substrings(s):
    leng = len(s)
    return [s[i:j] for i in range(leng) for j in range(i + 1, leng + 1)]

def counts(s):
    subs = substrings(s)
    result = set(subs)
    return len(result)

print(counts(S))