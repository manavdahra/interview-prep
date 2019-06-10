package dp;

/**
 * Author: B0204046
 * Date: 20/08/18 22:40
 */
public class LPS {

    private static boolean isPalindrome(char[] chars) {
        int i = 0, j = chars.length - 1;
        while (i <= j) {
            if (chars[i++] != chars[j--]) {
                return false;
            }
        }

        return true;
    }

    /**
     * Longest palindrome sub sequence in a given string
     * @param args
     */
    public static void main(String[] args) {
        System.out.println(isPalindrome("adbba".toCharArray()));
    }

    private static char[] lps(char[] chars, int beg, int end) {
        for (int i = beg; i < end; i++) {
            // isPalindrome(chars, beg, i)
        }
        return null;
    }
}
