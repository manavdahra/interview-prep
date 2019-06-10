package numbers;

/**
 * Author: B0204046
 * Date: 31/01/19 14:12
 */
public class CommonFactors {

    public static void main(String[] args) {
        System.out.println(solution(new int[] {2, 1, 2}, new int[] {1, 2, 2}));
    }

    public static int solution(int[] A, int[] B) {
        // write your code in Java SE 8
        int count = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] == B[i]) {
                count++;
            } else {
                int gcd = gcd(A[i], B[i]);
                long lcm = ((long) A[i] * (long) B[i]) / gcd;
                int small = Math.min(A[i], B[i]);
                int uncommon = (int) lcm / small;
                int gcd2 = gcd(uncommon, small);
                System.out.println("small " + small + " uncommon " + uncommon + " gcd " + gcd2);
                if (gcd2 > 1) {
                    count++;
                }
            }
        }
        return count;
    }

    private static int gcd(int a, int b) {
        if (a == b) {
            return a;
        }

        if (a > b) {
            return gcd(a - b, b);
        } else {
            return gcd(a, b - a);
        }
    }
}
