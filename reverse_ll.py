class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def print(self) -> str:
        s = ''
        node = self
        while node:
            s += str(node.val) + '->'
            node = node.next
        s += 'NULL'
        print(s)

"""
head = 1->2->3->4->5->None
head = 4
nextNode = 5
res = 5

""" 
def reverse(head: Node):
    if not head: return None
    if not head.next: return head

    nextNode = head.next
    res = reverse(nextNode)
    nextNode.next = head
    head.next = None
    return res

"""
       p  c  n
       v  v  v
head = 0->1->2->3->4->5->None

n = c.next
c.next = n.next
n.next = p.next
p.next = n

p     c  n
v     v  v
0->2->1->3->4->5->None

3->2->1->4->5->None
p           c
v           v
0->4->3->2->1->5->None
"""
def reverse2(head: Node):
    if not head: return None
    prev = Node(0, head)
    curr = prev.next
    
    while curr.next:
        next = curr.next
        curr.next = next.next
        next.next = prev.next
        prev.next = next
    
    return prev.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head.print()
rev = reverse(head)
rev.print()

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head.print()
rev = reverse2(head)
rev.print()