package arrays;

/**
 * Author: B0204046
 * Date: 06/06/19 17:18
 */
public class BoardGame {

    public static void main(String[] args) {
        char[][] arr = new char[3][5];
        arr[0][0] = 'E';
        arr[0][1] = 'W';
        arr[0][2] = 'W';
        arr[0][3] = 'W';
        arr[0][4] = 'E';

        arr[1][0] = 'W';
        arr[1][1] = 'B';
        arr[1][2] = 'B';
        arr[1][3] = 'B';
        arr[1][4] = 'W';

        arr[2][0] = 'E';
        arr[2][1] = 'W';
        arr[2][2] = 'W';
        arr[2][3] = 'W';
        arr[2][4] = 'E';


        int[][] visited = new int[arr.length][arr[0].length];
        int[][] movements = new int[4][2];
        movements[0] = new int[]{0, 1};
        movements[1] = new int[]{1, 0};
        movements[2] = new int[]{0, -1};
        movements[3] = new int[]{-1, 0};
        System.out.println(isCaptured(arr, visited, movements, 1, 2, 'B'));
    }

    public static boolean inBounds(char[][] arr, int x, int y) {
        int r = arr.length;
        int c = arr[0].length;

        return x < r && y < c && x >= 0 && y >= 0;
    }

    public static boolean isCaptured(char[][] arr, int[][] visited, int[][] movements, int x, int y, char color) {

        visited[x][y] = 1;
        System.out.println("At : " + x + " " + y + " " + color);

        for (int[] movement: movements) {
            int i = x + movement[0];
            int j = y + movement[1];
            if (!inBounds(arr, i, j) || visited[i][j] == 1) {
                continue;
            }

            if (arr[i][j] == 'E') {
                return false;
            }

            if (arr[i][j] == color) {
                boolean isCaptured = isCaptured(arr, visited, movements, i, j, color);
                if (!isCaptured) {
                    return false;
                }
            }
        }

        return true;
    }
}
