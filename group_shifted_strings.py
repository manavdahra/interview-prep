"""
Group Shifted Strings

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Input: strings = ["a"]
Output: [["a"]]

'abc'
'11'
'az' 25+96
'za' 1+96
def getHash(s):
    hash = ''
    for i in range(len(s)-1):
        ch1 = s[i]
        ch2 = s[i+1]
        hash += str((ord(ch2)-ord(ch1))%26+ord('a'))
    return hash
"""

import collections
from typing import List

def findGroups(strings: List[str]) -> List[str]:
    def getHash(s):
        hash = ''
        for i in range(len(s)-1):
            ch1 = s[i]
            ch2 = s[i+1]
            hash += str((ord(ch2)-ord(ch1))%26+ord('a'))
        return hash
    groups = collections.defaultdict(list)
    for s in strings:
        hash = getHash(s)
        groups[hash].append(s)
    return groups.values()

print(findGroups(["abc","bcd","acef","xyz","az","ba","a","z"]))
print(findGroups(["a"]))