S = list(map(str, input().split()))

if (S[0] == '<') and (S[1] == '<') and (S[2] == '<'):
    print('B')
elif (S[0] == '<') and (S[1] == '<') and (S[2] == '>'):
    print('C')
elif (S[0] == '<') and (S[1] == '>') and (S[2] == '<'):
    print('C')
elif (S[0] == '<') and (S[1] == '>') and (S[2] == '>'):
    print('A')
elif (S[0] == '>') and (S[1] == '<') and (S[2] == '<'):
    print('B')
elif (S[0] == '>') and (S[1] == '<') and (S[2] == '>'):
    print('B')
elif (S[0] == '>') and (S[1] == '>') and (S[2] == '<'):
    print('C')
elif (S[0] == '>') and (S[1] == '>') and (S[2] == '>'):
    print('B')