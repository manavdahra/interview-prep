package numbers;

/**
 * Author: B0204046
 * Date: 26/01/19 19:08
 */
public class CountFactors {

    public static void main(String[] args) {
        CountFactors countFactors = new CountFactors();
        System.out.println(countFactors.solution(15));
        System.out.println(countFactors.solution(75));
    }

    public int solution(int N) {
        // write your code in Java SE 8
        return factors(N);
    }

    private int factors(int N) {
        int factors = 0;
        long i = 1;
        while (i * i < N) {
            if (N % i == 0) {
                factors += 2;
            }
            i++;
        }
        if (i * i == N) {
            factors += 1;
        }

        return factors;
    }

}
