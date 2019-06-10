package algo;

/**
 * Author: B0204046
 * Date: 15/01/19 10:51
 */
public class FrogRiver {

    public static void main(String[] args) {
        System.out.println(solution(5, new int[] {1, 3, 1, 4, 2, 3, 5, 4}));
    }

    private static int solution(int X, int[] A) {
        int sum = 0;
        int i = 0;
        int[] counts = new int[X];
        while (sum < X && i < A.length) {
            if (counts[A[i] - 1] == 0) {
                counts[A[i] - 1]++;
                sum += counts[A[i] - 1];
            }
            i++;
        }
        if (sum == X) {
            return i - 1;
        } else {
            return -1;
        }
    }
}
