"""
Battleships in a Board

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Input: board = [["."]]
Output: 0
"""

from typing import List


def battleships(board: List[List[str]]) -> int:
    moves = [
        [0,1],
        [1,0]
    ]

    def dfs(r, c):
        board[r][c] = '.'
        for move in moves:
            x = r + move[0]
            y = c + move[1]
            if x >= len(board) or y >= len(board[x]): continue
            if board[x][y] != 'X': continue

            board[x][y] = '.'
            dfs(x, y)
    
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'X': continue
            dfs(i, j)
            count += 1
    return count

print(battleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print(battleships([["."]]))
    