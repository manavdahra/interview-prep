"""
Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    def print(self):
        self.items = []
        def preorder(node):
            if not node: return

            self.items.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        print(self.items)

"""
s = 4(2(3)(1))(6(5))
stack = [4,2]
num = ''
node = 2
"""
def constructBTree(s: str) -> TreeNode:
    stack = []
    num = ''
    for ch in s:
        if ch in '-' or ch.isdigit():
            num += ch
        else:
            if num:
                stack.append(TreeNode(int(num)))
                num = ''
            if ch == ')':
                node = stack.pop()
                if stack:
                    top = stack[-1]
                    if not top.left:
                        top.left = node
                    else:
                        top.right = node
    if num: 
        stack.append(TreeNode(int(num)))
    
    if not stack: return None
    
    return stack.pop()

root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5))).print()
copy = constructBTree('4(2(3)(1))(6(5))')
if not copy: print(None)
copy.print()