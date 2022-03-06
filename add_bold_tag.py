"""
Add Bold Tag in String

You are given a string s and an array of strings words. You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words. If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag. If two substrings wrapped by bold tags are consecutive, you should combine them.

Return s after adding the bold tags.

found = 0
s = ''
s += '<b>'
s += '</b>'
indexes = [1,1,1,0,0,0,1,1,1]
Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"

Input: s = "aaabbcc", words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"

"""

from typing import List

"""
length of string = n
num of words = w
max length of each word = m

O(m*n*w)
O(n)

     0
s = 'abcxyz123'
words = ['abc', '123']
indexes = [1,1,1,0,0,0,1,1,1]
"""
def addBoldTag(s: str, words: List[str]) -> str:
    indexes = [False]*len(s)

    for w in words:
        start = s.find(w)
        end = len(w)
        while start != -1:
            curr = start
            while curr < start+end:
                indexes[curr] = True
                curr += 1
            start = s.find(w, start+1)
    
    found = False
    ans = ''
    for i in range(len(indexes)):
        if indexes[i] and not found:
            found = True
            ans += '<b>'
        elif not indexes[i] and found:
            found = False
            ans += '</b>'
        ans += s[i]
    if found:
        ans += '</b>'
    return ans

print(addBoldTag('abcxyz123', ['abc', '123']))
print(addBoldTag('aaabbcc', ["aaa","aab","bc"]))