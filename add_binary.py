"""
Add Binary

Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
"""

def addBinaryStrings(s1: str, s2: str):
    i, j = len(s1)-1, len(s2)-1

    s = ''
    carry = 0
    while i >= 0 or j >= 0:
        a, b = 0, 0
        if i >= 0:
            a = int(s1[i])
        if j >= 0:
            b = int(s2[j])
        summ = (a + b + carry)%2
        carry = (a + b + carry)//2
        s = str(summ) + s
        i -= 1
        j -= 1
    
    if carry > 0:
        s = str(carry) + s
    return s

print(addBinaryStrings('1010', '1011'))
print(addBinaryStrings('11', '1'))

