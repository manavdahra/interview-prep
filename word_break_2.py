"""
Word Break 2

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""

from typing import List

"""
s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
"""
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    def helper(string, mem={}):
        if string in mem: return mem[string]
        if len(string) == 0: 
            return []
        
        breaks = []
        for w in wordDict:
            if string.startswith(w):
                if len(w) == len(string):
                    breaks.append(w)
                else:
                    res = helper(string[len(w):], mem)
                    for i in range(len(res)):
                        breaks.append(w + ' ' + res[i])
        mem[string] = breaks
        return mem[string]
    
    return helper(s)

print(wordBreak('catsanddog', ["cat","cats","and","sand","dog"]))
print(wordBreak('pineapplepenapple', ["apple","pen","applepen","pine","pineapple"]))
print(wordBreak('catsandog', ["cat","cats","and","sand","dog"]))