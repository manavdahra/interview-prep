package queue;

/**
 * Author: B0204046
 * Date: 10/11/18 18:43
 */
public class Queue {

    Item head;
    Item tail;

    public Queue() {}

    public void push(int data) {
        Item item = new Item();
        item.data = data;
        item.prev = null;

        if (head == null) {
            item.next = null;
            head = item;
            tail = item;
            return;
        }

        item.next = head;
        head = item;
    }

    public Item pop() {
        if (tail == null) {
            return null;
        }

        if (head == tail) {
            Item t = tail;
            head = null;
            tail = null;
            return t;
        }

        Item item = tail;
        tail = tail.prev;
        return item;
    }
}
