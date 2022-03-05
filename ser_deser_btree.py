"""
Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

                1
            2       3
                  4     5
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Input: root = []
Output: []
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        arr = []
        def preorder(node):
            if not node:
                return
            arr.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        print(arr)

class Solution:
    def __init__(self) -> None:
        pass

    """
    [1,2,3,null,null,4,5]
    s = 1,2,None,None,3,4,None,None,5
    1,2,None,None,3,4,None,None,5,None,None
    """
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return 'None'

        def helper(node):
            if not node: return 'None'

            s = str(node.val)
            s += ',' + helper(node.left)
            s += ',' + helper(node.right)
            return s
        
        return helper(root)

    def deserialize(self, data: str) -> TreeNode:
        self.index = 0
        def helper(nodes):
            if self.index >= len(nodes): return None
            if nodes[self.index] == 'None': return None

            node = TreeNode(int(nodes[self.index]))
            self.index += 1
            node.left = helper(nodes)
            self.index += 1
            node.right = helper(nodes)
            return node
        
        return helper(data.split(','))

root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
root.print()

sol = Solution()
data = sol.serialize(root)
print(data)
copy = sol.deserialize(data)
copy.print()
