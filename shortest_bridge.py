"""
Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Input: grid = [[0,1],[1,0]]
Output: 1

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""

from typing import List


moves = [
    [0,1],
    [1,0],
    [0,-1],
    [-1,0],
]
def findShores(grid: List[List[int]], r: int, c: int) -> List[int]:
    shores = set()
    q = [(r, c)]
    while q:
        x, y = q.pop(0)
        grid[x][y] = 2
        for move in moves:
            i = x + move[0]
            j = y + move[1]
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]): continue
            if grid[i][j] == 2: continue
            if grid[i][j] == 0: 
                shores.add((i, j, 0))
                continue
            grid[i][j] = 2
            q.append((i, j))
        
    return shores

def bfs(grid: List[List[int]], q: List[int], target: int) -> int:
    visited = set()
    while q:
        (x, y, d) = q.pop(0)
        visited.add((x, y))
        if grid[x][y] == target:
            return d

        for move in moves:
            i = x + move[0]
            j = y + move[1]
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]): continue
            if (i, j) in visited: continue
            visited.add((i, j))
            q.append((i, j, d+1))
        
    return -1

def shortestBridge(grid: List[List[int]]) -> int:
    r, c = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                r = i
                c = j
                break
    
    shores = findShores(grid, r, c)
    return bfs(grid, list(shores), 1)

"""
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,1,0,1],
[1,0,0,0,1],
[1,1,1,1,1]
"""
print(shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))