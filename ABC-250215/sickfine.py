s, t = input().split()

if (s == 'sick') and (t == 'fine'):
    print(2)
elif (s == 'fine') and (t == 'sick'):
    print(3)
elif (s == 'fine') and (t == 'fine'):
    print(4)
elif (s == 'sick') and (t == 'sick'):
    print(1)


