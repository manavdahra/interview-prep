package stacks;

/**
 * Author: B0204046
 * Date: 10/11/18 19:11
 */
public class SetOfStacks {

    Stack top;
    int size;
    int threshold;

    public SetOfStacks(int threshold) {
        this.threshold = threshold;
        top = new Stack(size + "");
        size++;
    }

    public void push(int data) {
        if (top.getSize() + 1 > threshold) {
            Stack prev = top;
            top = new Stack(size + "");
            top.next = prev;
            if (prev != null) {
                prev.prev = top;
            }
            size++;
        }

        top.push(data);
    }

    public Item pop() {
        if (top == null) {
            return null;
        }

        Item item = top.pop();
        if (top.getSize() == 0) {
            top = top.next;
            top.prev = null;
            size--;
        }
        return item;
    }

    public void print() {
        Stack current = top;
        while (current != null) {
            current.print();
            current = current.next;
        }
    }

    public static void main(String[] args) {
        SetOfStacks setOfStacks = new SetOfStacks(3);
        setOfStacks.push(1);
        setOfStacks.push(2);
        setOfStacks.push(3);

        setOfStacks.push(4);
        setOfStacks.push(5);
        setOfStacks.push(6);

        setOfStacks.push(7);
        setOfStacks.push(8);

        setOfStacks.pop();
        setOfStacks.print();
    }
}
