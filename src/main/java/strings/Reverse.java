package strings;

/**
 * Author: B0204046
 * Date: 08/11/18 14:36
 */
public class Reverse {

    public static void main(String[] args) {
        char [] str = { 'a', 'b', 'c', 'd', '\0'};
        System.out.println(str);
        reverse(str);
        System.out.println(str);
    }

    private static void reverse(char[] str) {
        int i = 0;
        int j = str.length - 2;
        while (i <= j) {
            swap(str, i, j);
            i++;
            j--;
        }
    }

    private static void swap(char[] str, int i, int j) {
        char ch = str[i];
        str[i] = str[j];
        str[j] = ch;
    }
}
