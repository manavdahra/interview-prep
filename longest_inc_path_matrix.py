"""
Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Input: matrix = [[1]]
Output: 1
"""

from typing import List

def longestIncPath(grid: List[List[int]]) -> int:
    moves = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0],
    ]

    visited = set()
    def dfs(r, c, mem={}):
        if (r, c) in mem: return mem[r,c]
        visited.add((r, c))

        maxPathLen = 0
        for move in moves:
            x = r + move[0]
            y = c + move[1]
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]): continue
            if (x, y) in visited: continue
            if grid[x][y] <= grid[r][c]: continue
            if (x, y) in mem: 
                maxPathLen = max(maxPathLen, mem[x,y])
                continue
            maxPathLen = max(maxPathLen, dfs(x, y))
        
        visited.remove((r, c))
        mem[r,c] = 1+maxPathLen
        return mem[r,c]

    maxPathLen = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            maxPathLen = max(maxPathLen, dfs(i, j))
    
    return maxPathLen

print(longestIncPath([[9,9,4],[6,6,8],[2,1,1]]))
print(longestIncPath([[3,4,5],[3,2,6],[2,2,1]]))