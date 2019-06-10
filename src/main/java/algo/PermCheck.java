package algo;

/**
 * Author: B0204046
 * Date: 15/01/19 10:14
 */
public class PermCheck {

    public static void main(String[] args) {
        System.out.println(solution(new int[] {0, 1, 3, 2}));
    }

    private static int solution(int[] A) {
        int[] counts = new int[A.length];

        for (int i : A) {
            if (i > A.length || i <= 0) {
                return 0;
            }
            if (counts[i - 1] > 0) {
                return 0;
            }
            counts[i - 1]++;
        }

        int product = 1;
        for (int i : counts) {
            product *= i;
        }

        return product;
    }

}
