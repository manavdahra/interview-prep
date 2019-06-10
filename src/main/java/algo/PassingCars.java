package algo;

/**
 * Author: B0204046
 * Date: 15/01/19 13:21
 */
public class PassingCars {

    public static void main(String[] args) {
        System.out.println(solution(new int[] {0, 1, 0, 1, 1}));
    }

    private static int solution(int[] A) {
        int i = A.length - 1;
        int ones = 0;
        Long pairs = 0L;
        while (i >= 0) {
            if (A[i] > 0) {
                ones++;
            } else {
                pairs += ones;
                if (pairs > 1000000000) {
                    return -1;
                }
            }
            i--;
        }

        return pairs.intValue();
    }
}
