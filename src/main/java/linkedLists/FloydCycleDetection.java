package linkedLists;

/**
 * Author: B0204046
 * Date: 10/11/18 17:57
 */
public class FloydCycleDetection {

    public static void main(String[] args) {
        Node head = new Node(6);
        Node second = new Node(5, 6);
        Node tail = head.tail();
        Node secondTail = second.tail();

        tail.next = second;
        secondTail.next = tail;

        printNodes(head, 15);

        Node loopedNode = findLoopedNode(head);
        System.out.println(loopedNode.data);
    }

    public static void printNodes(Node head, int threshold) {
        Node current = head;
        int counter = 0;
        while (current != null && counter < threshold) {
            System.out.print(current.data + " -> ");
            current = current.next;
            counter++;
        }
        System.out.println("NULL");
    }

    private static Node findLoopedNode(Node head) {
        Node slow = head;
        Node fast = head;

        do {
            slow = slow.next;
            fast = fast.next;
            fast = fast.next;
        } while (slow != fast);

        fast = head;
        while (fast != slow) {
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}
