N = list(map(int, input().split()))
S = input()

print(S[N[1]:N[0]-N[2]])

# import java.util.Scanner;

# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // N[0], N[1], N[2] を読み込む
#         int[] N = new int[3];
#         for (int i = 0; i < 3; i++) {
#             N[i] = sc.nextInt();
#         }
#         sc.nextLine(); // 改行を消費

#         // 文字列を読み込む
#         String S = sc.nextLine();

#         // 部分文字列を出力（N[1]文字目から、N[0] - N[2] 文字目の手前まで）
#         System.out.println(S.substring(N[1], N[0] - N[2]));
#     }
# }
