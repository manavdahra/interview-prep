"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

from typing import List

"""
maxlen(w) = m
len(wordDict) = d
len(s) = n

O(d^n)
"""
def wordBreak(s: str, wordDict: List[str]) -> bool:
    def helper(string: str, mem={}) -> bool:
        if len(string) == 0: return True

        if string in mem: return mem[string]

        mem[string] = False
        for word in wordDict:
            if not string.startswith(word): continue
            if helper(string[len(word):], mem): 
                mem[string] = True
                break
        
        return mem[string]
    
    return helper(s)

print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak('applepenapple', ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))