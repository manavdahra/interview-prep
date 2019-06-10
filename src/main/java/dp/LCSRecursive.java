package dp;

/**
 * Author: B0204046
 * Date: 10/08/18 20:22
 */
public class LCSRecursive {

    /**
     * Given -> ABCDGH
     *          AEDFHR
     *
     * lcs is -> reverse of (h,d,b) => bdh
     * @param args
     */

  public static void main(String[] args) {
    String s1 = "ABCDGH";
    String s2 = "AEDFHR";

    System.out.println(lcs(s1, s2));

  }

  public static String lcs(String s1, String s2) {
      if (s1.length() <= 1) {
          if (s2.contains(s1)) {
              return s1;
          }
          return "";
      }

      return lcs(s1.substring(0, s1.length() - 1), s2) + lcs(s1.substring(s1.length() - 1), s2);
  }
}
