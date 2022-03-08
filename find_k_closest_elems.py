"""
Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

"""

from typing import List


def kClosestElems(arr: List[int], k: int, x: int) -> List[int]:
    lo, hi = 0, len(arr)-k
    while lo < hi:
        mid = lo + (hi-lo)//2
        if x-arr[mid] > arr[mid+k]-x:
            lo = mid+1
        else:
            hi = mid
    return arr[lo:lo+k]

print(kClosestElems([1,2,3,4,5], 4, 3))
print(kClosestElems([1,2,3,4,5], 4, -1))
print(kClosestElems([1,2,3,4,5], 2, -1))
print(kClosestElems([1,2,3,4,5], 2, 5))
print(kClosestElems([0,0,1,2,3,3,4,7,7,8], 1, 6))
print(kClosestElems([0,0,1,2,3,3,4,7,7,8], 3, 5))