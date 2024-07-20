from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    a = [ord(char) - ord('a') for char in s]
    a.sort()
    ans = 0

    while True:
        ok = True
        for i in range(n - k + 1):
            flag = True
            for j in range(k):
                if a[i + j] != a[i + k - 1 - j]:
                    flag = False
                    break
            if flag:
                ok = False
                break
        if ok:
            ans += 1
        if not next_permutation(a):
            break
    
    print(ans)

def next_permutation(seq):
    """Transform seq to its next permutation in-place. Return False if there are no further permutations."""
    i = len(seq) - 2
    while i >= 0 and seq[i] >= seq[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = len(seq) - 1
    while seq[i] >= seq[j]:
        j -= 1
    seq[i], seq[j] = seq[j], seq[i]
    seq[i + 1:] = reversed(seq[i + 1:])
    return True

if __name__ == "__main__":
    main()
