package linkedLists;

/**
 * Author: B0204046
 * Date: 09/11/18 15:22
 */
public class Node {

    int data;
    Node next;

    public Node() {
    }

    public Node(int size) {
        this(size, 0);
    }

    public Node(int size, int offset) {
        Node current = this;
        current.data = offset;
        for (int i = 1; i < size; i++) {
            Node node = new Node();
            node.data = i + offset;
            current.next = node;
            current = current.next;
        }
    }

    public void add(int data) {
        Node last = this;
        while (last.next != null) {
            last = last.next;
        }

        Node newNode = new Node();
        newNode.data = data;
        last.next = newNode;
    }

    public void add(Node newNode) {
        Node last = this;
        while (last.next != null) {
            last = last.next;
        }
        last.next = newNode;
    }

    public void printNodes() {
        Node current = this;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("NULL");
    }

    public Node tail() {
        Node tail = this;
        while (tail.next != null) {
            tail = tail.next;
        }
        return tail;
    }

    public int size() {
        Node head = this;
        int size = 0;
        while (head != null) {
            head = head.next;
            size++;
        }

        return size;
    }
}
