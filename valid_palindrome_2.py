"""
Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false
"""

def isValidPalindrome(s: str) -> bool:
    def checkPalindrome(beg, end):
        if beg >= end: return True

        while beg < end:
            if s[beg] != s[end]: return False
            beg += 1
            end -= 1
        return True
    
    i, j = 0, len(s)-1

    while i < j:
        if s[i] == s[j]: 
            i += 1
            j -= 1
            continue
        return checkPalindrome(i+1, j) or checkPalindrome(i, j-1)
    
    return True

testCases = [
    ['aba', True],
    ['abca', True],
    ['abc', False],
]

for t in testCases:
    actual = isValidPalindrome(t[0])
    print('Expected: {}, Actual: {}'.format(t[1], actual))
