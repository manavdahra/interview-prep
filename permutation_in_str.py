"""
Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""

def getFreq(s: str):
    freq = {}
    for ch in s: 
        if not ch in freq:
            freq[ch] = 0
        freq[ch] += 1
    
    return freq

def compareFreq(freq1, freq2):
    if len(freq1) != len(freq2): return False

    for k in freq1:
        if not k in freq2: return False
        if freq1[k] != freq2[k]: return False
    
    return True

"""
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
i = 0
j = 4
freq1 = {a: 1, b: 1}
freq2 = {b:1, a: 1}

"""
def hasPermutation(s1: str, s2: str) -> bool:
    i = 0
    j = len(s1)-1
    freq1 = getFreq(s1)
    freq2 = getFreq(s2[:len(s1)])

    while j < len(s2):
        if compareFreq(freq1, freq2): return True

        j += 1
        if j >= len(s2): break
        if s2[j] not in freq2:
            freq2[s2[j]] = 0
        freq2[s2[j]] += 1
        freq2[s2[i]] -= 1
        if freq2[s2[i]] == 0: 
            freq2.pop(s2[i])
        i += 1
    
    return compareFreq(freq1, freq2)

print(hasPermutation('ab', 'eidbaooo'))
print(hasPermutation('ab', 'eidboaoo'))