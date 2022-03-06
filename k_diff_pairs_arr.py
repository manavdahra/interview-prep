"""
K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
nums[i] - nums[j] == k
Notice that |val| denotes the absolute value of val.

{
    5: 1,
    1: 1,
    3: 1,
    -1: 1,
    6: 1,
    2: 1,
}
count = 1

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
"""

from typing import List

from sympy import Q

"""
nums = [3,1,4,1,5], k = 2
possiblePair = {3,-1,6,2,3}
count = 2

nums = [1,2,3,4,5], k = 1
possiblePair = {0,1,2,3,4,6}
count = 4

"""
def kDiffPairs(nums: List[int], k: int) -> int:
    freq = {}

    count = 0
    for n in nums:
        if not n in freq: 
            freq[n] = 0
        freq[n] += 1

    for n in freq:
        if k > 0 and n+k in freq:
            count += 1
        elif k == 0 and freq[n] > 1:
            count += 1
    return count

print(kDiffPairs([3,1,4,1,5], 2))
print(kDiffPairs([1,2,3,4,5], 1))
print(kDiffPairs([1,3,1,5,4], 0))