package dp;

/**
 * Author: B0204046
 * Date: 13/08/18 16:33
 */
public class CoinChange {
    public static void main(String[] args) {
        System.out.println(count(4, new int[] { 1, 2, 3 }, 3));
    }

    private static int count(int total, int[] denominations, int index) {
        if (total == 0) {
            return 1;
        }

        if (total < 0) {
            return 0;
        }

        if (index <= 0) {
            return 0;
        }

        return count(total, denominations, index - 1) + count(total - denominations[index - 1], denominations, index);
    }
}
