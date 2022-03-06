"""
Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Input: num = 982456
output: 986452

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Input: num = 9973
Output: 9973
Explanation: No swap.


"""
"""
num = 982456
maxDigits = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 8,
    5: 9,
}
digits = []
"""
from sympy import python


def maxSwap(num: int) -> int:
    digits = []
    x = num
    while x > 0:
        digits.append(x%10)
        x = x//10

    digits.reverse()
    
    maxDigits = {}
    maxDigit = -1
    pos = -1
    i = len(digits)-1
    while i >= 0:
        if digits[i] > maxDigit:
            maxDigit = digits[i]
            pos = i
        maxDigits[i] = pos
        i -= 1
    
    i = 0
    j = -1
    while i < len(digits)-1:
        if digits[i] < digits[maxDigits[i+1]]:
            j = maxDigits[i+1]
            break
        i += 1
    digits[i], digits[j] = digits[j], digits[i]
    return int(''.join(str(d) for d in digits))

print(maxSwap(982456))
print(maxSwap(9973))
print(maxSwap(2736))