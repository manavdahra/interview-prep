package strings;

/**
 * Author: B0204046
 * Date: 08/11/18 16:49
 */
public class Duplicates {

    public static void main(String[] args) {
        String str = "manavdahra";
        char[] chars = str.toCharArray();
        removeDuplicates(chars);
    }

    private static void removeDuplicates(char[] chars) {
        int bits = 0;
        int duplicates = 0;
        for (int i = 0; i < chars.length - duplicates; i++) {
            int offset = 1 << (chars[i] - 'a');
            if ((bits & offset) > 0) {
                duplicates++;
                for (int j = i; j < chars.length; j++) {
                    if (j < chars.length - 1) {
                        chars[j] = chars[j + 1];
                    }
                }
            }
            bits |= offset;
        }
        System.out.println(duplicates);
        for (int i = 0; i < chars.length - duplicates; i++) {
            System.out.print(chars[i]);
        }
    }
}
