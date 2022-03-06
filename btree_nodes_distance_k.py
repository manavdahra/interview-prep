"""
All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

                3
            5       1
        6    2     0    8
           7   4
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Input: root = [1], target = 1, k = 3
Output: []

"""
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kDistNodes(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    graph = collections.defaultdict(list)

    def dfs(node, parent):
        if not node: return

        graph[node].append(parent)
        if node.left:
            graph[node].append(node.left)
            dfs(node.left, node)
        if node.right:
            graph[node].append(node.right)
            dfs(node.right, node)
    
    dfs(root, None)

    seen = set()
    q = [(target, 0)]
    ans = []
    while q:
        node, dist = q.pop(0)
        seen.add(node)
        if dist == k:
            ans.append(node.val)
            continue
        
        for neib in graph[node]:
            if not neib: continue
            if neib in seen: continue
            seen.add(neib)
            q.append((neib, dist+1))
    
    return ans

"""
                3
            5       1
        6    2     0    8
           7   4
"""
target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
print(kDistNodes(root, target, 2))

target = TreeNode(1)
root = target
print(kDistNodes(root, target, 3))
