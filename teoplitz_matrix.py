"""
Toeplitz Matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
[1,2,3,4],
[5,1,2,3],
[9,5,1,2]

9 -> (2,0) i-j = 2
5,5 -> (1,0),(2,1) i-j=1
1,1,1 -> (0,0),(1,1),(2,2) i-j = 0
2,2,2 -> (0,1),(1,2),(2,3) i-j = -1

In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.


"""

from typing import List

"""
[1,2,3,4],
[5,1,2,3],
[9,5,1,2]

group = {
    0: 1,
    -1: 2,
    -2: 3,
    -3: 4,
    1: 5,
    2: 9,
}

"""
def isTeoplitz(mat: List[List[int]]) -> bool:
    group = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i-j in group:
                if group[i-j] != mat[i][j]: return False
            else:
                group[i-j] = mat[i][j]
    
    return True

print(isTeoplitz([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(isTeoplitz([[1,2],[2,2]]))