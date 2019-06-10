package dp;

/**
 * Author: B0204046
 * Date: 11/08/18 11:55
 */
public class StringEditCost {

    public static void main(String[] args) {
        //
        String s1 = "geek";
        String s2 = "gesek";

        String lcs = LCSRecursive.lcs(s1, s2);
        int cost = Math.max(s1.length(), s2.length()) - lcs.length();
        System.out.println(cost);
    }
}
