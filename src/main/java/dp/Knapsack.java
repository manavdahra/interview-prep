package dp;

/**
 * Author: B0204046
 * Date: 19/08/18 02:15
 */
public class Knapsack {

    private static int[] value = {60, 100, 120};
    private static int[] weight = {10, 20, 30};
    private static int w = 50;
    private static int[][] dp = new int[value.length + 1][w + 1];

    public static void main(String[] args) {
        System.out.println(knapsack(value, weight, value.length, w));
        for (int i = 0; i <= value.length; i++) {
            for (int j = 0; j <= w; j++) {
                System.out.print(dp[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static int knapsack(int[] value, int[] weight, int n, int w) {

        for (int i = 0; i <= value.length; i++) {
            for (int j = 0; j <= w; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                }
                else if (weight[i-1] <= j) {
                    dp[i][j] = Math.max(value[i-1] + dp[i-1][j-weight[i-1]], dp[i-1][j]);
                }
                else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        return dp[n][w];
    }
}
