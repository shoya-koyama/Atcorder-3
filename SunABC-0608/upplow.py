s = input()

low_cnt = sum(map(str.islower, s))
sup_cnt = sum(map(str.isupper, s))

if sup_cnt > low_cnt:
    print(s.upper())
else:
    print(s.lower())