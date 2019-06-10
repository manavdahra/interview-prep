package dp;

/**
 * Author: B0204046
 * Date: 10/07/18 14:39
 */
public class FibonacciTabulation {

  private static int fib(int n, int[] arr) {

    if (arr == null) {
      arr = new int[n+1];
    }

    arr[0] = 0; arr[1] = 1;
    for (int i = 2; i <= n; i++) {
      arr[i] = arr[i-1] + arr[i-2];
    }

    return arr[n];
  }

  public static void main(String[] args) {
    int n = 10000;
    long start = System.currentTimeMillis();
    int result = fib(n, null);
    long end = System.currentTimeMillis();
    System.out.printf("Fib of %d is: %d in: %d", n, result, (end - start));
  }
}
