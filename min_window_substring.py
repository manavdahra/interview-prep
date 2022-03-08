"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


"""

import sys


def compareFreq(freq1, freq2):
    for k in freq2:
        if k not in freq1: return False
        if freq1[k] < freq2[k]: return False
    return True

def getFreq(s: str):
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    return freq

"""
s = "ADOBECODEBANC"
t = "ABC"

i = 0
j = 3
t_freq = {
    A: 1,
    B: 1,
    C: 1,
}
freq = {
    D: 1,
    O: 1,
    B: 1,
    E: 1,
    C: 1
}
minWindowLen = 6
minWindow = 'ADOBEC'

"""
def minWindow(s: str, t: str) -> str:
    t_freq = getFreq(t)
    i = 0
    j = len(t_freq)-1
    freq = getFreq(s[i:len(t_freq)])

    minWindowLen = sys.maxsize
    minWindow = ''
    while i <= j and j < len(s):
        if compareFreq(freq, t_freq):
            if minWindowLen > (j-i+1):
                minWindowLen = j-i+1
                minWindow = s[i:j+1]
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                freq.pop(s[i])
            i += 1
            continue
        j += 1
        if j >= len(s): break
        if s[j] not in freq:
            freq[s[j]] = 0
        freq[s[j]] += 1
    
    if compareFreq(freq, t_freq):
        if minWindowLen > (j-i):
            minWindowLen = j-i
            minWindow = s[i:j]
    
    if minWindow == sys.maxsize: return ''
    return minWindow

print(minWindow('ADOBECODEBANC', 'ABC'))
print(minWindow('wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon', 'ozgzyywxvtublcl'))
print(minWindow('a', 'a'))
print(minWindow('a', 'b'))
print(minWindow('a', 'ba'))