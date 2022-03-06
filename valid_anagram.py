"""
Valid anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""

def validAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    freq1 = {}
    for ch in s:
        if ch not in freq1:
            freq1[ch] = 0
        freq1[ch] += 1
    
    freq2 = {}
    for ch in t:
        if ch not in freq2:
            freq2[ch] = 0
        freq2[ch] += 1

    if len(freq1) != len(freq2): return False

    for k in freq1:
        if k not in freq2: return False
        if freq1[k] != freq2[k]: return False
    
    return True

print(validAnagram('anagram', 'nagaram'))
print(validAnagram('car', 'ccar'))