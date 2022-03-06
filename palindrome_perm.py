"""
Palindrome permutation

Given a string s, return true if a permutation of the string could form a palindrome.

Input: s = "code"
Output: false

Input: s = "aab"
Output: true

Input: s = "carerac"
Output: true

Input: s = "decareraced"
Output: true
"""

def canFormPalindrome(s: str) -> bool:
    freq = [0]*26
    for ch in s:
        freq[ord(ch)-ord('a')] += 1
    
    odds = 0
    for f in freq:
        if odds > 1: return False
        if f%2 != 0: odds +=1
    
    return True

print(canFormPalindrome('a'))
print(canFormPalindrome(''))
print(canFormPalindrome('decareraced'))
print(canFormPalindrome('dddeeeaabbcc'))