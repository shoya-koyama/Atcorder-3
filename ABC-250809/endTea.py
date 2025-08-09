N = int(input())
S = input()

if S.endswith('tea'):
  print('Yes')
else:
  print('No')

N = int(input())
S = input()

if len(S) >= 3 and S[-3:] == 'tea':
    print('Yes')
else:
    print('No')
