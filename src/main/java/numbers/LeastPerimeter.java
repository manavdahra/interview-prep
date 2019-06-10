package numbers;

/**
 * Author: B0204046
 * Date: 26/01/19 19:35
 */
public class LeastPerimeter {
    public static void main(String[] args) {
        LeastPerimeter leastPerimeter = new LeastPerimeter();
        System.out.println(leastPerimeter.solution(15486451));
    }

    public int solution(int N) {
        // write your code in Java SE 8
        int k = (int) Math.pow(N, 0.5);
        int A = k, B = k;
        while (A >= 1 && B <= N) {
            if (A * B == N) {
                return 2 * (A + B);
            } else if (A * B < N) {
                A++;
            } else if (A * B > N) {
                B--;
            }
        }
        return 2 * (A + B);
    }
}
