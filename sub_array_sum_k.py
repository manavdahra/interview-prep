"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2

[1,2,3]

a0 + a1 + .... + aj + aj+1 + aj+2 + ... an + an+1 + ... + am

Input: nums = [1,2,3], k = 3
Output: 2
"""

from typing import List

"""
nums = [1,1,1] k = 2
prefix = [1,2,3]
sumSet = {2,3}
count = 2
"""
def subArraySumEqualsK(nums: List[int], k: int) -> int:
    prefix = []
    psum = 0
    for num in nums:
        psum += num
        prefix.append(psum)
    
    sumDict = {k:1}
    count = 0
    for psum in prefix:
        if psum in sumDict:
            count += sumDict[psum]
        if psum+k not in sumDict:
            sumDict[psum+k] = 1
        else:
            sumDict[psum+k] += 1
    
    return count

testCases = [
    [[1,2,3], 3, 2],
    [[1,1,1], 2, 2],
    [[2,3,5,1,6,8,2,1], 10, 2],
    [[1,-1,0], 0, 3],
]

for t in testCases:
    actual = subArraySumEqualsK(t[0], t[1])
    print('Expected: {}, Actual: {}'.format(t[2], actual))