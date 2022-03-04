"""
Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
"""

import collections
from typing import List


def makeLargeIsland(grid: List[List[int]]) -> int:
    moves = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]
    def dfs(r, c, group):
        grid[r][c] = group

        count = 1
        for move in moves:
            x = r + move[0]
            y = c + move[1]
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
                continue
            if grid[x][y] == group or grid[x][y] == 0: continue

            grid[x][y] = group
            count += dfs(x, y, group)
        return count
    
    groupId = 2
    areas = collections.defaultdict(int)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                areas[groupId] = dfs(i, j, groupId)
                groupId += 1
    
    # print(areas, grid)
    maxArea = 0 if len(areas) == 0 else max(areas.values())
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                tot = 1
                seen = set()
                for move in moves:
                    r = i + move[0]
                    c = j + move[1]
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]): continue
                    if grid[r][c] in seen: continue
                    if grid[r][c] in areas:
                        tot += areas[grid[r][c]]
                        seen.add(grid[r][c])
                maxArea = max(maxArea, tot)
    return maxArea

print(makeLargeIsland([[1,0],[0,1]]))
print(makeLargeIsland([[1,1],[1,0]]))
print(makeLargeIsland([[1,1],[1,1]]))
print(makeLargeIsland([[1,1,1,1,0],[1,0,0,0,0],[0,0,0,1,1],[1,1,0,1,0],[0,0,0,0,1]]))