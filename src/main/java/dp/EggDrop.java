package dp;

/**
 * Author: B0204046
 * Date: 20/08/18 11:12
 */
public class EggDrop {

    private static int[][] dp = null;

    public static void main(String[] args) {
        int n = 2;
        int k = 36;
        dp = new int[n+1][k+1];
        System.out.println(eggDrop(n, k));
    }

    private static int eggDrop(int n, int k) {
        if (dp[n][k] > 0) {
            System.out.println("n: " + n + " k: " + k + " dp: " + dp[n][k]);
            return dp[n][k];
        }

        if (k == 1 || k == 0) {
            dp[n][k] = k;
            return dp[n][k];
        }

        if (n == 1) {
            dp[n][k] = k;
            return dp[n][k];
        }

        int min = Integer.MAX_VALUE - 1;
        for (int i = 1; i <= k; i++) {
            int max = Math.max(eggDrop(n - 1, i - 1), eggDrop(n, k - i));
            if (max < min) {
                min = max;
            }
        }

        return min + 1;
    }
}
