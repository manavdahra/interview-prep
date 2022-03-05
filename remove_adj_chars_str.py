"""
Remove All Adjacent Duplicates In String

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Input: s = "abbbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Input: s = "azxxzy"
Output: "ay"
"""

def removeAdjCharacters(s: str) -> str:
    stack = []
    for ch in s:
        if stack and stack[-1][0] == ch:
            _, freq = stack[-1]
            if freq+1 >= 2:
                stack.pop()
                continue
            stack[-1] = (ch, freq+1)
        else:
            stack.append((ch, 1))
    return ''.join([ch*freq for ch, freq in stack])
print(removeAdjCharacters('abbaca'))
print(removeAdjCharacters('azxxzy'))