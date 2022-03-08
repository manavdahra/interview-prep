"""
Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


"""

def regexp(s: str, p: str) -> bool:
    def dp(i, j, mem={}):
        if (i, j) in mem: return mem[i,j]
        
        if i >= len(s) or j >= len(p):
            if i >= len(s) and j >= len(p): return True
            elif i < len(s) and j >= len(p): return False
        
        firstMatch = i < len(s) and p[j] in {s[i], '.'}
        if j+1 < len(p) and p[j+1] == '*':
            mem[i,j] = dp(i, j+2, mem) or firstMatch and dp(i+1, j, mem)
        else:
            mem[i,j] = firstMatch and dp(i+1, j+1, mem)
        return mem[i,j]

    return dp(0, 0)

print(regexp('ab', '.*'))
print(regexp('aa', 'a*'))
print(regexp('aa', '..'))
print(regexp('aahkqjwelkksdasdhasuidhiqe', 'aa.*lk*sd.*qe'))
print(regexp('aahkqjwelkksdasdhasuidhiqe', 'aa.*lk*sd.*.qe'))