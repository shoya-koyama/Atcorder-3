N = int(input())
D = list(map(int, input().split()))

for i in range(N-1):
    count = 0
    result = []
    for j in range(i, N-1):
        if j == i:
            count += D[i]
            result.append(D[i])
        else:
            count += D[j]
            result.append(count)
    final = ' '.join(map(str, result))
    print(final)

# import java.util.*;

# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // 入力の読み取り
#         int N = sc.nextInt();
#         int[] D = new int[N];
#         for (int i = 0; i < N; i++) {
#             D[i] = sc.nextInt();
#         }

#         // ロジックの実装
#         for (int i = 0; i < N - 1; i++) {
#             int count = 0;
#             List<Integer> result = new ArrayList<>();
#             for (int j = i; j < N - 1; j++) {
#                 if (j == i) {
#                     count += D[i];
#                     result.add(D[i]);
#                 } else {
#                     count += D[j];
#                     result.add(count);
#                 }
#             }
#             // 結果の出力（スペース区切り）
#             for (int k = 0; k < result.size(); k++) {
#                 if (k > 0) System.out.print(" ");
#                 System.out.print(result.get(k));
#             }
#             System.out.println();
#         }
#     }
# }
