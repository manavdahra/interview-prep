"""
Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.

"""

import collections
from plot_tree import TreeNode

def deepestSubtree(root: TreeNode) -> TreeNode:
    if not root: return None
    leaves = collections.defaultdict(list)
    parents = {}
    def dfs(node, depth, parent):
        if not node: return
        if not node.left and not node.right:
            leaves[depth].append(node)
        
        parents[node] = parent
        dfs(node.left, depth+1, node)
        dfs(node.right, depth+1, node)
    
    dfs(root, 0, None)
    keys = sorted(leaves.keys(), key=lambda x: -x)
    
    count = {}
    for l in leaves[keys[0]]:
        node = l
        while node:
            if node not in count: 
                count[node] = 0
            count[node] += 1
            if count[node] == len(leaves[keys[0]]):
                return node
            node = parents[node]
    return None

"""
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
"""
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)), )
root.visualise()

res = deepestSubtree(root)
res.visualise()

