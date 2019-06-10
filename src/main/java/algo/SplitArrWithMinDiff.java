package algo;

/**
 * Author: B0204046
 * Date: 14/01/19 18:21
 */
public class SplitArrWithMinDiff {

    public static void main(String[] args) {
        System.out.print(minDiff(new int[] {-1000, 1000}));
    }

    private static int minDiff(int[] A) {
        long leftSum = 0;
        long totalSum = 0;
        for (int i: A) {
            totalSum += i;
        }

        Long minDiff = Long.MAX_VALUE;
        for (int i = 0; i < A.length - 1; i++) {
            leftSum += A[i];
            long rightSum = totalSum - leftSum;
            if (minDiff > Math.abs(leftSum - rightSum)) {
                minDiff = Math.abs(leftSum - rightSum);
            }
        }

        return minDiff.intValue();
    }
}
