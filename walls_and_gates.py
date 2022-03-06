"""
Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Input: rooms = 
[
    [inf,   -1,     0,      inf],
    [inf,   inf,    inf,    -1],
    [inf,   -1,     inf,    -1],
    [0,     -1,     inf,    inf]
]
[(0,2),(3,0)]
[(3,0),(0,3),(1,2)]
[(0,3),(1,2),(2,0)]
[(0,3),(1,2),(2,0)]
Output: 
[
    [3,     -1,     0,      1],
    [2,     2,      1,      -1],
    [1,     -1,     2,      -1],
    [0,     -1,     3,      4],
]
"""

from typing import List


def wallsAndGates(grid: List[List[int]]):
    q = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                q.append((i, j, 0))
    
    empty = 2**31-1
    while q:
        r, c, d = q.pop(0)
        for move in [[0,1],[1,0],[0,-1],[-1,0]]:
            x = r + move[0]
            y = c + move[1]
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]): continue
            if grid[x][y] <= 0 or grid[x][y] != empty: continue
            grid[x][y] = d+1
            q.append((x, y, d+1))

grid = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
wallsAndGates(grid)
print(grid)

grid = [[-1]]
wallsAndGates(grid)
print(grid)