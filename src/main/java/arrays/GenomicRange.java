package arrays;

import java.util.HashMap;
import java.util.Map;

/**
 * Author: B0204046
 * Date: 18/01/19 13:58
 */
public class GenomicRange {

    public static void main(String[] args) {
        int[] minValues = solution("CAGCCTA", new int[] {2, 5, 0}, new int[] {4, 5, 6});
        for (int i = 0; i < minValues.length; i++) {
            System.out.print(minValues[i] + " ");
        }
    }

    private static Map<String, Integer> genomics = new HashMap<>();
    private static int[][] mins = new int[1000][1000];

    static {
        genomics.put("A", Integer.valueOf("1"));
        genomics.put("C", Integer.valueOf("2"));
        genomics.put("G", Integer.valueOf("3"));
        genomics.put("T", Integer.valueOf("4"));
    }

    public static int[] solution(String S, int[] P, int[] Q) {
        int[] solution = new int[P.length];
        for (int i = 0; i < P.length; i++) {
            int start = P[i];
            int end = Q[i];

            int min = Integer.MAX_VALUE;
            if (start <= 1 && end <= 1) {
                min = minValue(S, start, end);
            } else {
                while (start <= end) {
                    if (min > genomics.get(S.charAt(start) + "")) {
                        min = genomics.get(S.charAt(start) + "");
                    }
                    start++;
                }
            }

            solution[i] = min;
        }
        return solution;
    }

    private static int minValue(String S, int start, int end) {
        if (start > end) {
            return Integer.MAX_VALUE;
        }
        if (start == end) {
            mins[start][end] = genomics.get(S.charAt(start) + "");
            return mins[start][end];
        }

        if (mins[start][end] == 0) {
            int min = Math.min(Math.min(genomics.get(S.charAt(start) + ""), genomics.get(S.charAt(end) + "")),
                    minValue(S, start + 1, end - 1));
            mins[start][end] = Integer.valueOf(min + "");
        }
        return mins[start][end];
    }
}
