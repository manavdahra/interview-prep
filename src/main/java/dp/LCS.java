package dp;

/**
 * Author: B0204046
 * Date: 10/08/18 19:23
 */
public class LCS {

    /**
     * Given -> ABCDGH
     *          AEDFHR
     *
     *      a b c d g h
     *
     * a    1 1 1 1 1 1
     * e    1 1 1 1 1 1
     * d    1 1 1 2 2 2
     * f    1 1 1 2 2 2
     * h    1 1 1 2 2 3
     * r    1 1 1 2 2 3
     *
     * lcs is -> reverse of (h,d,b) => bdh
     * @param args
     */

    public static void main(String[] args) {

        String s1 = "ABCDGH";
        String s2 = "AEDFHR";

        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();

        int[][] A = new int[c2.length][];

        for (int i = 0; i < c2.length; i++) {
            A[i] = new int[c1.length];
        }

        System.out.println(lcs(c1, c2, A));
    }

    public static String lcs(char[] s1, char[] s2, int[][] A) {
        for (int i = 0; i < s2.length; i++) {
            for (int j = 0; j < s1.length; j++) {
                if (s2[i] == s1[j]) {
                    A[i][j] = getLeftDiagonal(A, i, j) + 1;
                } else {
                    A[i][j] = Math.max(getLeft(A, i, j), getTop(A, i, j));
                }
            }
        }

        // for (int i = 0; i < s2.length; i++) {
        //     for (int j = 0; j < s1.length; j++) {
        //         System.out.print(A[i][j]);
        //     }
        //     System.out.println();
        // }

        return getLcs(s1, s2, A);
    }

    private static String getLcs(char[] s1, char[] s2, int[][] A) {

        StringBuilder lcs = new StringBuilder();
        int i = A.length - 1;
        int j = A[i].length - 1;

        while (i >= 0 && j >= 0) {
            if (getLeftDiagonal(A, i, j) < A[i][j]) {
                lcs.append(s1[j]);
                j--;
                i--;
            } else if (getLeft(A, i, j) == A[i][j]) {
                j--;
            } else if (getTop(A, i, j) == A[i][j]) {
                i--;
            }
        }

        return lcs.reverse().toString();
    }

    private static int getLeftDiagonal(int[][] A, int i, int j) {
        if (i == 0 || j == 0) {
            return 0;
        }

        return A[i-1][j-1];
    }

    private static int getLeft(int[][] A, int i, int j) {
        if (j == 0) {
            return 0;
        }

        return A[i][j-1];
    }

    private static int getTop(int[][] A, int i, int j) {
        if (i == 0) {
            return 0;
        }

        return A[i-1][j];
    }
}
