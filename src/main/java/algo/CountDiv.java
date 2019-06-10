package algo;

/**
 * Author: B0204046
 * Date: 15/01/19 13:43
 */
public class CountDiv {

    public static void main(String[] args) {
        System.out.println(solution(1, 2000000000, 3));
    }

    private static int solution(int A, int B, int K) {
        int a = (A % K) > 0 ? A + K - (A % K) : A;
        int an = (B % K) > 0 ? B - (B % K) : B;
        return ((an - a) / K) + 1;
    }
}
