package algo;

/**
 * Author: B0204046
 * Date: 14/01/19 17:49
 */
public class FrogJmp {

    public static void main(String[] args) {
        System.out.println(solution(10, 85, 30));
    }

    private static int solution(int x, int y, int D) {
        Double jmps = Math.ceil((double)(y - x) / D);
        return jmps.intValue();
    }
}
