package numbers;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Author: B0204046
 * Date: 29/01/19 20:23
 */
public class Eratosthenes {

    public static void main(String[] args) {
        int[] F = getF(100);
        // Arrays.stream(F).forEach(e -> System.out.print(e + " "));
        // System.out.println();
        System.out.println(factors(15, F));
        System.out.println(factors(75, F));
    }

    private static int[] getF(int n) {
        int[] F = new int[n + 1];
        int i = 2;
        while (i * i <= n) {
            if (F[i] == 0) {
                int k = i * i;
                while (k <= n) {
                    F[k] = i;
                    k += i;
                }
            }
            i++;
        }
        return F;
    }

    private static boolean[] primes(int n) {
        boolean[] primes = new boolean[n + 1];
        Arrays.fill(primes, true);
        int i = 2;
        while (i * i <= n) {
            if (primes[i]) {
                int j = i * i;
                while (j <= n) {
                    primes[j] = false;
                    j += i;
                }
            }
            i++;
        }
        return primes;
    }

    private static Set<Integer> factors(int n, int[] F) {
        Set<Integer> factors = new HashSet<>();
        while (F[n] > 0) {
            factors.add(F[n]);
            n = n / F[n];
        }
        factors.add(n);
        return factors;
    }
}
