"""
Valid number:

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

at least one digit should be present - hasDigit
. should occur at most once - hasDot
+/- sign can occur at most twice but only at the beginning or just after the exp symbol (e, E) - 
any other character aprat from e,E is invalid - 
no dot after exponent
exponent can occur at most once - hasExp


Input: s = "0"
Output: true

Input: s = "e"
Output: false

Input: s = "."
Output: false
"""

"""
valid
-.9
0089
3e+7
-90E3

invalid
1e
-+3
95a54e53
"""
def isValid(s: str) -> bool:
    hasDigit, hasDot, hasExp = False, False, False

    for i, ch in enumerate(s):
        if ch.isdigit():
            hasDigit = True
        elif ch == '.':
            if hasDot or hasExp: return False
            hasDot = True
        elif ch in '+-':
            if i > 0 and s[i-1] not in 'eE': return False
        elif ch in 'eE':
            if hasExp or not hasDigit: return False
            hasExp = True
            hasDigit = False
        else:
            return False
    
    return hasDigit

print(isValid('0'))
print(isValid('-.9'))
print(isValid('0089'))
print(isValid('3e+7'))
print(isValid('-90E3'))
print(isValid('-2.'))

print(isValid('1e'))
print(isValid('-+3'))
print(isValid('95a54e53'))
print(isValid('e'))
print(isValid('.'))
