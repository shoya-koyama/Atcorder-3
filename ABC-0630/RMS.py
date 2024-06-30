s = input()

idr = s.find('R')
idm = s.find('M')

if idr < idm:
    print('Yes')
else:
    print('No')