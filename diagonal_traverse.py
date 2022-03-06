"""
Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Explanation:

[1,2,3]
[4,5,6]
[7,8,9]
[1] -> [2,4] -> [7,5,3] -> [6,8] -> [9]
"""

import collections
from typing import List


def diagTraverse(mat: List[List[int]]):
    groups = collections.defaultdict(list)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            groups[i+j].append(mat[i][j])
    ans = []
    for k in groups:
        diag = groups[k]
        if k % 2 == 0:
            diag = diag[::-1]
        ans.extend(diag)
    return ans

print(diagTraverse([[1,2,3],[4,5,6],[7,8,9]]))
    