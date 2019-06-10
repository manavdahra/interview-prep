package stacks;

/**
 * Author: B0204046
 * Date: 10/11/18 18:30
 */
public class Stack {

    String name;
    Item top;
    int size;
    Stack next;
    Stack prev;

    public Stack(String name) {
        this.name = name;
    }

    public Item peek() {
        return top;
    }

    public Item pop() {
        if (top == null) {
            return null;
        }

        Item item = top;
        top = top.next;
        size--;
        return item;
    }

    public void push(int data) {
        Item item = new Item();
        item.data = data;
        item.next = top;
        top = item;
        size++;
    }

    public void print() {
        System.out.println("Stack:" + name);
        Item current = top;
        while (current != null) {
            System.out.println(current.data);
            current = current.next;
        }
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int getSize() {
        return size;
    }

    public static void main(String[] args) {
        Stack stack = new Stack("0");
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.print();

        stack.pop();
        stack.print();

        System.out.println(stack.getSize());
    }
}
