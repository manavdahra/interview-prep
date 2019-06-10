package stacks;

/**
 * Author: B0204046
 * Date: 10/11/18 22:47
 */
public class SortStack {

    public static void main(String[] args) {
        Stack stack = new Stack("1");
        stack.push(3);
        stack.push(2);
        stack.push(4);
        stack.push(1);
        stack.push(5);

        stack.print();
        Stack sortedStack = sort(stack);
        sortedStack.print();
    }

    private static Stack sort(Stack original) {
        Stack sorted = new Stack("2");
        while (!original.isEmpty()) {
            Item item = original.pop();
            while (!sorted.isEmpty() && sorted.peek().data > item.data) {
                original.push(sorted.pop().data);
            }
            sorted.push(item.data);
        }

        return sorted;
    }
}
