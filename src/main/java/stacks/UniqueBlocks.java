package stacks;

import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

/**
 * Author: B0204046
 * Date: 19/01/19 11:36
 */
public class UniqueBlocks {

    public static void main(String[] args) {
        System.out.println(solution(new int[] {1, 1, 1}));
    }

    public static int solution(int[] H) {
        // write your code in Java SE 8
        int i = 0;
        Stack<Integer> stack = new Stack<>();
        int blocks = 0;
        while (i < H.length) {

            Set<Integer> uniques = new HashSet<>();
            int top = stack.empty() ? -1 : stack.peek();

            while (top > H[i] && !stack.empty()) {
                uniques.add(stack.pop());
                top = stack.empty() ? -1 : stack.peek();
            }
            stack.push(H[i]);
            blocks += uniques.size();
            i++;
        }

        Set<Integer> uniques = new HashSet<>();
        while (!stack.empty()) {
            uniques.add(stack.pop());
        }

        return blocks + uniques.size();
    }
}
