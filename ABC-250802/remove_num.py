N = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N[1]):
    if B[i] in A:
        A.remove(B[i])
    else:
        pass
    
result = ' '.join(map(str, A))
print(result)

# import java.util.*;

# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // N[0] = Aの要素数, N[1] = Bの要素数
#         int[] N = new int[2];
#         for (int i = 0; i < 2; i++) {
#             N[i] = sc.nextInt();
#         }

#         // Aの読み込み
#         List<Integer> A = new ArrayList<>();
#         for (int i = 0; i < N[0]; i++) {
#             A.add(sc.nextInt());
#         }

#         // Bの読み込み
#         int[] B = new int[N[1]];
#         for (int i = 0; i < N[1]; i++) {
#             B[i] = sc.nextInt();
#         }

#         // Bの各要素について、Aにあれば削除
#         for (int i = 0; i < N[1]; i++) {
#             if (A.contains(B[i])) {
#                 A.remove(Integer.valueOf(B[i])); // 値として削除
#             }
#         }

#         // 出力
#         for (int i = 0; i < A.size(); i++) {
#             System.out.print(A.get(i));
#             if (i < A.size() - 1) {
#                 System.out.print(" ");
#             }
#         }
#         System.out.println();
#     }
# }
