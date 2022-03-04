"""
Random Pick with Weight

You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
"""

import random
from typing import List


class Solution:
    """
    weights = [1, 3, 2, 4, 5]
    self.prob = [0.066, 0.266, 0.4, 0.667, 1]
    tot = 15
    """
    def __init__(self, weights: List[int]):
        self.prob = []
        tot = sum(weights)
        curr_sum = 0
        for w in weights:
            curr_sum += w
            self.prob.append(curr_sum/tot)
    
    """
    lo = 2
    hi = 2
    mid = 1
    """
    def pickIndex(self) -> int:
        val = random.random()
        lo = 0
        hi = len(self.prob)-1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if val > self.prob[mid]:
                lo = mid+1
            else:
                hi = mid
        return lo

solution = Solution([1, 3])
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())