package linkedLists;

/**
 * Author: B0204046
 * Date: 09/11/18 16:22
 */
public class AddNumbers {

    public static void main(String[] args) {
        Node n1 = new Node();
        n1.data = 3;
        n1.add(1);
        n1.add(5);

        Node n2 = new Node();
        n2.data = 5;
        n2.add(9);
        n2.add(2);

        n1.printNodes();

        n2.printNodes();

        Node n3 = addNumbers(n1, n2);
        n3.printNodes();
    }

    private static Node addNumbers(Node h1, Node h2) {
        Node n1 = h1;
        Node n2 = h2;
        Node n3 = null;

        int carry = 0;
        while (n1 != null || n2 != null) {
            int sum = (n1 != null ? n1.data : 0) + (n2 != null ? n2.data : 0) + carry;
            int remainder = sum % 10;
            carry = sum >= 10 ? 1 : 0;
            if (n3 == null) {
                n3 = new Node();
                n3.data = remainder;
            } else {
                n3.add(remainder);
            }
            n1 = n1 != null ? n1.next : null;
            n2 = n2 != null ? n2.next : null;
        }

        if (carry > 0) {
            n3.add(carry);
        }

        return n3;
    }
}
