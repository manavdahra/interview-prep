package arrays;

/**
 * Author: B0204046
 * Date: 20/01/19 00:23
 */
public class MaxProfit {

    public static void main(String[] args) {
        // System.out.println(solution(new int[] {23171, 21011, 21123, 21366, 21013, 21367}));
        System.out.println(solution(new int[] {0, 21011}));
    }

    public static int solution(int[] A) {
        // write your code in Java SE 8
        if (A.length == 0) {
            return 0;
        }

        int[] B = new int[A.length - 1];
        for (int i = 0; i < A.length - 1; i++) {
            B[i] = A[i + 1] - A[i];
        }

        int maxEnding = 0, maxSlice = 0;
        for (int i: B) {
            maxEnding = Math.max(0, maxEnding + i);
            maxSlice = Math.max(maxEnding, maxSlice);
        }
        return maxSlice;
    }

}
