"""
Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Input: s = "3+2*2"
Output: 7

Input: s = " 3/2 "
Output: 1

Input: s = " 3+5 / 2 "
Output: 5

s = "3+2*2"
stack = [3,2]
positive = True
num = ''
val = 2
"""

def calc(s: str) -> int:
    num = ''
    stack = []
    op = '+'
    for ch in s:
        if ch == ' ': continue
        if ch.isdigit():
            num += ch
        else:
            if op == '+':
                stack.append(int(num))
            elif op == '-':
                stack.append(-1*int(num))
            elif op == '*':
                last = stack.pop()
                stack.append(last*int(num))
            elif op == '/':
                last = stack.pop()
                stack.append(last // int(num))
            num = ''
            op = ch
    if num:
        if op == '+':
            stack.append(int(num))
        elif op == '-':
            stack.append(-1*int(num))
        elif op == '*':
            last = stack.pop()
            stack.append(last*int(num))
        elif op == '/':
            last = stack.pop()
            stack.append(last // int(num))
    return sum(stack)

print(calc('3+2*2/1'))
print(calc('3+2*2/5'))
