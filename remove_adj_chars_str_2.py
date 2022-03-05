"""
Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""

def removeDuplicates(s: str, k: int) -> str:
    stack = []
    for ch in s:
        if stack and stack[-1][0] == ch:
            _, freq = stack[-1]
            if freq+1 >= k:
                stack.pop()
                continue
            stack[-1] = (ch, freq+1)
        else:
            stack.append((ch, 1))
    return ''.join([ch*freq for ch, freq in stack])

print(removeDuplicates('pbbcggttciiippooaais', 2))
            
