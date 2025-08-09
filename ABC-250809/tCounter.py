S = input()

t_counter = 0
x = 0
lst = []
string_lst = []
result = 0

for i in range(len(S)):
  if S[i] == 't':
    t_counter += 1
    lst.append(i)
    
if len(lst) != 0:
  for j in range(lst[0], len(S)):
    string_lst.append(S[j])
    if len(S) < 3:
      result = 0
    if S[j] == 't':
      x += 1
    if j >= 3:
      tmp = (x-2) / (len(string_lst) - 2)
      if result < tmp:
        result = tmp
  
print(round(result, 17))


S = input().strip()
n = len(S)
result = 0.0

for i in range(n):
    if S[i] != 't':
        continue

    for j in range(i + 2, n):
        if S[j] != 't':
            continue

        x = sum(1 for k in range(i, j + 1) if S[k] == 't')
        tmp = (x - 2) / (j - i + 1 - 2)
        if result < tmp:
            result = tmp

print(f"{result:.17f}")
