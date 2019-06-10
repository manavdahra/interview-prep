package arrays;

/**
 * Author: B0204046
 * Date: 26/08/18 09:59
 */
public class SpiralTraverse {

    private static int[][] arr = {
            { 1, 2, 3 },
            { 4, 5, 6 },
            { 7, 8, 9 },
            // { 10, 11, 12 }
    };

    public static void main(String[] args) {
        spiralTraverse(arr);
    }

    private static void spiralTraverse(int[][] arr) {

        int count = 0,
                d = 0,
                i = 0,
                j = 0,
                t = 0,
                b = arr.length - 1,
                l = 0,
                r = arr[arr.length - 1].length - 1;

        while (count < arr.length * arr[arr.length-1].length) {
            if (hasHitBound(i, j, t, b, l, r)) {
                if (d == 0) {
                    t++;
                    j--; // backtrack
                    i++;
                } else if (d == 1) {
                    r--;
                    i--; // backtrack
                    j--;
                } else if (d == 2) {
                    b--;
                    j++; // backtrack
                    i--;
                } else if (d == 3) {
                    l++;
                    i++; // backtrack
                    j++;
                }
                d = (d + 1) % 4;
            }
            System.out.print(arr[i][j] + " ");
            if (d == 0) {
                j++;
            } else if (d == 1) {
                i++;
            } else if (d == 2) {
                j--;
            } else if (d == 3) {
                i--;
            }
            count++;
        }

    }

    private static boolean hasHitBound(int i, int j, int t, int b, int l, int r) {
        return i < t || i > b || j < l || j > r;
    }
}
