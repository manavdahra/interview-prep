package dp;

/**
 * Author: B0204046
 * Date: 10/07/18 14:26
 */
public class FibonacciMemoization {

  private static int fib(int n, int[] arr) {

    if (arr == null) {
      arr = new int[n+1];
    }

    if (n <= 0) {
      return 0;
    } else if (n == 1) {
      return 1;
    }

    if (arr[n] != 0) {
      return arr[n];
    }

    int val = fib(n-2, arr) + fib(n-1, arr);
    arr[n] = val;
    return val;
  }

  /**
   * Fib series:
   * 0 1 1 2 3 5 8 13 21 34 55 ...
   * @param args
   */
  public static void main(String[] args) {
    int n = 10000;
    long start = System.currentTimeMillis();
    int result = fib(n, null);
    long end = System.currentTimeMillis();
    System.out.printf("Fib of %d is: %d in: %d", n, result, (end - start));
  }

}
