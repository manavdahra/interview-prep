"""

Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.


Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

from typing import List
from heapq import heappush, heappop

def kthLargestElement(nums: List[int], k: int) -> int:
    heap = []
    for num in nums: # O (n) -> O(nlog(n-k))
        heappush(heap, -num) # O(log(n-k+1))
        if len(heap) > len(nums)-k+1:
            heappop(heap)  # O(1)
    return -1*heappop(heap)

print(kthLargestElement([3,2,1,5,6,4], 2))
print(kthLargestElement([3,2,3,1,2,4,5,5,6], 4))

