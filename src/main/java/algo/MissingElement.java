package algo;

/**
 * Author: B0204046
 * Date: 14/01/19 18:04
 */
public class MissingElement {

    public static void main(String[] args) {
        int[] arr = new int[] {1, 3, 4, 5};
        System.out.println(missingElement(arr, 4));
    }

    private static long missingElement(int[] A, int N) {
        double sum = 0;
        for (int i: A) {
            sum += i;
        }
        double expectedSum = (double)((N + 1) * (N + 2))/ 2;

        Double e = expectedSum - sum;
        return e.intValue();
    }
}
