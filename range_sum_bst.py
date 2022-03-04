"""
Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

                10
            5       15
    3       7           18

Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum = 0
        def traverse(node: TreeNode):
            if not node: return

            if node.val < low:
                traverse(node.right)
            elif node.val > high:
                traverse(node.left)
            else:
                self.sum += node.val
                traverse(node.left)
                traverse(node.right)
    
        traverse(root)
        return self.sum

root1 = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
testCases = [
    [root1, 7, 15, 32],
]

soln = Solution()
for t in testCases:
    actual = soln.rangeSumBST(t[0], t[1], t[2])
    print('Expected: {}, Actual: {}'.format(t[3], actual))

