import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    def visualise(self) -> None:
        m = collections.defaultdict(list)
        self.depth, self.minWidth, self.maxWidth = -1, 0, 0
        def buildHashTable(node, r, c):
            if not node: return
            self.depth = max(self.depth, r)
            self.minWidth = min(self.minWidth, c)
            self.maxWidth = max(self.maxWidth, c)
            m[r, c].append(str(node.val))
            buildHashTable(node.left, r+1, c-1)
            buildHashTable(node.right, r+1, c+1)
        
        buildHashTable(self, 0, 0)
        width = self.maxWidth - self.minWidth + 1
        depth = self.depth + 1

        if depth <= 0 or width <= 0: return 
        grid = [['' for _ in range(width)] for _ in range(depth)]
        for r, c in m:
            newCol = c - self.minWidth
            if (r, c) in m:
                grid[r][newCol] += ' '.join([s for s in m[r,c]])
        
        # for r in range(len(grid)):
        #     items = []
        #     for c in range(len(grid[r])):
        #         items.append(grid[r][c])
        #     print('\t'.join(items))
