package backtrack;

/**
 * Author: B0204046
 * Date: 26/08/18 14:24
 */
public class StringPermutation {

    public static void main(String[] args) {
        char[] ch = {'a', 'b', 'c', 'd'};
        permute(ch, 0, ch.length);
    }

    private static void permute(char[] c, int beg, int end) {
        if (beg == end) {
            System.out.println(c);
        }

        for (int i = beg; i < end; i++) {
            swap(c, beg, i);
            permute(c, beg + 1, end);
            swap(c, beg, i);
        }
    }

    private static void swap(char c[], int a, int b) {
        char ch = c[a];
        c[a] = c[b];
        c[b] = ch;
    }
}
