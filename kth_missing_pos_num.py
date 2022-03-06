"""
Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array
              0,1,2,3,4
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
 0,1,2,3,4,5
[2,3,4,7,9,11] k = 5

k+hi+1

              0,1,2,3
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""

from typing import List

def kthMissingPosNum(nums: List[int], k: int) -> int:
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        val = nums[mid]-mid-1
        if val < k:
            lo = mid+1
        else:
            hi = mid-1
    return lo+k

print(kthMissingPosNum([2,3,4,7,11], 5))
print(kthMissingPosNum([1,2,3,4], 2))
print(kthMissingPosNum([2,3,4,7,9,11], 5))