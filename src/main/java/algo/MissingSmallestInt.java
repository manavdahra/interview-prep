package algo;

import java.util.Arrays;

/**
 * Author: B0204046
 * Date: 15/01/19 11:32
 */
public class MissingSmallestInt {

    public static void main(String[] args) {
        System.out.println(solution(new int[] { 1, 2, 3 }));
    }

    private static int solution(int[] A) {
        Arrays.sort(A);
        int missingElement = 1;
        for (int i: A) {
            if (i == missingElement) {
                missingElement++;
            }
        }
        return missingElement;
    }
}
