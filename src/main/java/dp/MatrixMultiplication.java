package dp;

/**
 * Author: B0204046
 * Date: 19/08/18 00:23
 */
public class MatrixMultiplication {

    private static int[] mats = { 10, 20, 30, 40, 30 };
    private static int[][] dp = new int[mats.length][mats.length];

    public static void main(String[] args) {
        System.out.println(minMatProd(mats, 0, mats.length - 1));
        for (int i = 0; i < mats.length; i++) {
            for (int j = 0; j < mats.length; j++) {
                System.out.print(dp[i][j] + "\t");
            }
            System.out.println();
        }
    }

    private static int minMatProd(int[] mats, int beg, int end) {
        if (dp[beg][end] > 0) {
            return dp[beg][end];
        }

        if (beg + 2 == end) {
            dp[beg][end] = mats[beg] * mats[beg + 1] * mats[end];
            return dp[beg][end];
        }

        dp[beg][end] = Math.min(
                mats[beg] * mats[beg + 1] * mats[end] + minMatProd(mats, beg + 1, end),
                minMatProd(mats, beg, end - 1) + mats[beg] * mats[end - 1] * mats[end]
        );
        return dp[beg][end];
    }
}
