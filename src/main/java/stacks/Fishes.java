package stacks;

import java.util.Stack;

/**
 * Author: B0204046
 * Date: 19/01/19 12:43
 */
public class Fishes {

    public static void main(String[] args) {
        System.out.println(solution(new int[] {4, 3, 2, 1, 5, 6}, new int[] {0, 1, 0, 0, 0, 1}));
    }

    public static int solution(int[] A, int[] B) {
        // write your code in Java SE 8
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        int lastDirection = 2;
        while (i < B.length) {
            if (B[i] == 1) {
                stack.push(A[i]);
                lastDirection = B[i];
            } else {
                int top = -1;
                if (!stack.empty()) {
                    top = stack.peek();
                }
                if (A[i] > top && B[i] < lastDirection) {
                    if (!stack.empty()) {
                        stack.pop();
                    }
                    stack.push(A[i]);
                    lastDirection = B[i];
                }
            }
            i++;
        }

        System.out.println(stack);
        return stack.size();
    }
}
