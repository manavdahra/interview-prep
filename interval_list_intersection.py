"""
Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""

from typing import List

"""
[[0,2],[5,10],[13,23],[24,25]]
[[1,5],[8,12],[15,24],[25,26]]

[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""
def intersection(l1: List[int], l2: List[int]) -> List[int]:
    i = 0
    j = 0

    intersect = []
    while i < len(l1) and j < len(l2):
        [s1, e1] = l1[i]
        [s2, e2] = l2[j]

        if s2 > e1:
            i += 1
            continue
        elif s1 > e2:
            j += 1
            continue
        
        intersect.append([max(s1, s2), min(e1, e2)])
        if e1 <= e2:
            i += 1
        else:
            j += 1
    return intersect

print(intersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
