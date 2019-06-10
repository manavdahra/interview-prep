package arrays;

/**
 * Author: B0204046
 * Date: 14/01/19 16:47
 */
public class OddElement {

    public static void main(String[] args) {
        int [] arr = new int[] {7, 7, 2, 1, 1, 3, 3};
        System.out.println(solution(arr));
    }

    private static int solution(int[] A) {
        int oddElement = 0;
        for (int element : A) {
            oddElement = oddElement ^ element;
        }
        return oddElement;
    }
}
