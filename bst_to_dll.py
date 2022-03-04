"""
Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

root = [4,2,5,1,3]

            4
        2       5
    1     3

+-1-><-2-><-3-><-4-><-5-+
|                       |
+----------><-----------+

Output: [1,2,3,4,5]

root = [2,1,3]
[1,2,3]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstToDLL(root: TreeNode) -> TreeNode:
    def helper(node: TreeNode):
        if not node: return None

        leftDLL = bstToDLL(node.left)
        
        if leftDLL:
            while leftDLL and leftDLL.right:
                leftDLL = leftDLL.right
            leftDLL.right = node
            node.left = leftDLL

        rightDLL = bstToDLL(node.right)
        
        if rightDLL:
            while rightDLL and rightDLL.left:
                rightDLL = rightDLL.left
            rightDLL.left = node
            node.right = rightDLL
        
        return node
    
    helper(root)
    head = root
    while head.left:
        head = head.left
    
    tail = root
    while tail.right:
        tail = tail.right
    
    head.left = tail
    tail.right = head
    return head

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
bstToDLL(root)

