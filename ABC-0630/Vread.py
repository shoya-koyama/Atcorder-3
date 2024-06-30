S, T = input().split()
result = ''
label = False

for i in range(1, len(S)):
    n = i
    lst = [S[a:a+n] for a in range(0,len(S), n)]
    for j in range(len(lst)):
        result += lst[j][-1]
    if result == T:
        label = True
        break
    
if label == True:
    print('Yes')
else:
    print('No')
    
# def main():
#     S, T = input().split()
#     label = False

#     for w in range(1, len(S)):
#         for c in range(w):
#             now = ""
#             for i in range(c, len(S), w):
#                 now += S[i]
#             if now == T:
#                 label = True
#                 break
#         if label:
#             break
    
#     if label:
#         print('Yes')
#     else:
#         print('No')

# if __name__ == "__main__":
#     main()

