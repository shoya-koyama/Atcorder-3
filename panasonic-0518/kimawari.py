H = int(input())

kimawari = 0
i = 0

while kimawari <= H:
    kimawari += 2**i
    if kimawari > H:
        print(i+1)
        break
    i += 1

#C++
# #include <bits/stdc++.h>
# using namespace std;

# int main(){
#     int h;
#     cin >> h;
#     int ans = 0;
#     int now = 0;
#     while (now <= h) {
#         now += 1 << ans;
#         ans++;
#     }
#     cout << ans << endl;
# }
