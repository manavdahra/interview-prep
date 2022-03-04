"""
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""

def pow(x, n):
    def helper(x, n):
        if n == 0: return 1
        if n % 2 == 0:
            y = helper(x, n//2)
            return y*y
        else:
            y = helper(x, n//2)
            return x*y*y
    
    res = helper(x, abs(n))
    if n < 0:
        return 1/res
    return res

print(pow(2.0000, 10))
print(pow(2.1000, 3))
print(pow(2.0000, -2))