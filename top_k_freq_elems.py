"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

n(n+1)/2
Input: nums = [1,2,2,3,3,3,4,4,4,4], k = 2
Output: [1,2]

O(nlogn)
freq = {
    3: [1,4],
    2: [2],
    1: [3],
}

Input: nums = [1], k = 1
Output: [1]

"""

import collections
from heapq import heappop, heappush
from typing import List

"""
nums = [1,2,2,3,3,3,4,4,4,4], k = 2
freq = {1: 1, 2: 2, 3: 3, 4: 4}
heap = [(-1, 1)]
"""
def topKElems(nums: List[int], k: int) -> List[int]:
    if len(nums) == k: return nums
    
    freq = collections.defaultdict(int)
    for n in nums:
        freq[n] += 1
    
    heap = []
    for num in freq:
        heappush(heap, (freq[num], num))
        if len(heap) > k:
            heappop(heap)

    ans = []
    while heap:
        _, num = heappop(heap)
        ans.append(num)
    
    return ans

print(topKElems([1,2,2,3,3,3,4,4,4,4], 2))