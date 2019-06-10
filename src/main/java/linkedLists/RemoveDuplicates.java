package linkedLists;

/**
 * Author: B0204046
 * Date: 09/11/18 15:23
 */
public class RemoveDuplicates {

    public static void main(String[] args) {
        Node head = new Node(5);
        head.printNodes();

        head.add(2);
        head.add(1);
        head.add(3);
        head.add(2);
        head.printNodes();

        removeDuplicates(head);

        head.printNodes();
    }

    private static void removeDuplicates(Node head) {
        Node current = head;
        while (current != null) {
            Node runner = current.next;
            int data = current.data;
            if (runner != null) {
                Node prev = current;
                while (runner != null) {
                    if (runner.data == data) {
                        prev.next = runner.next;
                    } else {
                        prev = prev.next;
                    }
                    runner = runner.next;
                }
            }
            current = current.next;
        }
    }
}
