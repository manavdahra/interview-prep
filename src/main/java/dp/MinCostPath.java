package dp;

/**
 * Author: Manav
 * Date: 11/08/18 12:40
 */
public class MinCostPath {

    private static int[] costs = new int[3 * 3];

    public static void main(String[] args) {
        int[][] C = {
                {1, 2, 3},
                {4, 8, 2},
                {1, 5, 3}
        };

        System.out.println(LC(C, 2, 2));
        for (int i = 0; i < 9; i++) {
            System.out.print(costs[i] + " ");
        }
        System.out.println();
    }

    private static int LC(int[][] C, int r, int c) {

        if (r < 0 || c < 0) {
            return Integer.MAX_VALUE;
        } else if (r == 0 && c == 0) {
            return C[0][0];
        }

        if (costs[r * 3 + c] > 0) {
            return costs[r * 3 + c];
        }

        costs[r * 3 + c] = Math.min(LC(C, r - 1, c), Math.min(LC(C, r - 1, c - 1), LC(C, r, c - 1))) + C[r][c];
        return costs[r * 3 + c];
    }
}
