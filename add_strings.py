"""
Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
Input: num1 = "11", num2 = "123"
Output: "134"

Input: num1 = "456", num2 = "77"
Output: "533"

Input: num1 = "0", num2 = "0"
Output: "0"
"""

"""
456
77

3
"""
from numpy import add


def addStrings(num1: str, num2: str) -> str:
    i, j, carry = len(num1)-1, len(num2)-1, 0
    ans = ''
    while i >= 0 or j >= 0:
        # print(i, j)
        a = 0
        if i >= 0:
            a = int(num1[i])
        b = 0
        if j >= 0:
            b = int(num2[j])
        summ = a + b + carry
        carry = summ // 10
        summ = summ % 10
        ans = str(summ) + ans
        i -= 1
        j -= 1

    if carry > 0:
        ans = str(carry) + ans
    return ans

testCases = [
    ['11', '123', '134'],
    ["456", "77", '533'],
    ["0", "0", '0'],
]

for t in testCases:
    actual = addStrings(t[0], t[1])
    print('Expected: {}, Actual: {}'.format(t[2], actual))