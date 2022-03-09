"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]

   p     c    n       
dummy -> 1 -> 2 -> 3 -> 4 -> None

while c and n:
    p.next = n
    c.next = n.next
    n.next = c

    p = c
    c = c.next
    n = c.next


head = [1,2,3,4]

"""
class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def print(self):
        s = ''
        node = self
        while node:
            s += str(node.val) + ' -> '
            node = node.next
        s += 'None'
        print(s)

def swapPairs(head: Node) -> Node:
    dummy = Node(0, head)
    prev = dummy
    curr = head
    while curr and curr.next:
        prev.next = curr.next
        curr.next = curr.next.next
        prev.next.next = curr

        prev = curr
        curr = curr.next
    
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head.print()
newHead = swapPairs(head)
newHead.print()

head = Node(1)
head.print()
newHead = swapPairs(head)
newHead.print()

newHead = swapPairs(None)
