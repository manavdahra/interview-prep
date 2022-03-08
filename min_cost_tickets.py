"""
Minimum Cost For Tickets

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

minCost(1) = min(2 + minCost(2), 7 + minCost(8), 15 + minCost(31))
minCost(1) = min(2 + minCost(2), 7 + minCost(5), 15)
minCost()
"""

from typing import List

"""
days = [1,4,6,7,8,20], costs = [2,7,5]
maxDay = 20
daysSet = {1,4,6,7,8,20}

helper(1) = min(2 + helper(4), 7 + helper(8), 15 + helper(31))
helper(4) = min(2 + helper(6), 7 + helper(11), 15 + helper(34))
"""
def minCost(days: List[int], costs: List[int]) -> int:
    maxDay = max(days)
    daysSet = set(days)
    def helper(day: int, mem={}) -> int:
        if day in mem: return mem[day]
        if day > maxDay: return 0
        if day not in daysSet: return helper(day+1, mem)

        mem[day] = min(
            costs[0] + helper(day+1, mem),
            costs[1] + helper(day+7, mem),
            costs[2] + helper(day+30, mem),
        )
        return mem[day]
    return helper(days[0])

print(minCost([1,4,6,7,8,20], [2,7,15]))

