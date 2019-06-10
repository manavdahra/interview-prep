package numbers;

/**
 * Author: B0204046
 * Date: 31/01/19 12:14
 */
public class Gcd {

    public static void main(String[] args) {
        System.out.println(gcd(7, 14));
    }

    public static int gcd(int a, int b) {
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
