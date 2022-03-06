"""
Remove islands

Given 2D matrix with 1s and 0s. 1 representing island and 0 representing water. We need to sink/remove all the islands
connected to boundary of matrix.
"""

from typing import List


def removeIslands(grid: List[List[int]]):
    def dfs(r, c):
        grid[r][c] = 0
        for move in [[0,1],[1,0],[0,-1],[-1,0]]:
            x = r + move[0]
            y = c + move[1]
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]): continue
            if grid[x][y] == 0: continue
            grid[x][y] = 0
            dfs(x, y)
    
    for i in range(len(grid)):
        if grid[i][0] == 1: dfs(i, 0)
        if grid[i][len(grid[i])-1] == 1: dfs(i, len(grid[i])-1)

    for j in range(len(grid[0])):
        if grid[0][j] == 1: dfs(0, j)
        if grid[len(grid)-1][j] == 1: dfs(len(grid)-1, j)

grid = [
    [1,0,0,0,0,1,1,1,0],
    [1,1,1,0,0,1,0,0,0],
    [1,0,0,1,0,1,1,1,0],
    [1,0,1,1,1,0,1,1,0],
    [1,1,0,1,0,1,1,0,0],
    [1,0,0,0,0,1,0,0,0],
]
removeIslands(grid)
for i in range(len(grid)):
    print(grid[i])

