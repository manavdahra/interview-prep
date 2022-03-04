"""
Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""

def balanceParanthesis(s: str) -> str:
    """
    lee(t(c)o)de)
    """
    stack = []
    for i, ch in enumerate(s):
        if ch not in '()': continue
        if stack and s[stack[-1]] == '(' and ch == ')':
            stack.pop()
        else:
            stack.append(i)
    
    """
    stack = [12]
    """
    ans = ''
    for i, ch in enumerate(s):
        if stack and stack[0] == i:
            stack.pop(0)
        else:
            ans += ch
    return ans

testCases = [
    ['lee(t(c)o)de)', 'lee(t(c)o)de'],
    ['a)b(c)d', 'ab(c)d'],
    ['))((', '']
]

for t in testCases:
    actual = balanceParanthesis(t[0])
    print('Expected: {}, Actual: {}'.format(t[1], actual))

