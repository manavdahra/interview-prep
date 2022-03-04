"""
Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Input: s = "()())()"
Output: ["(())()","()()()"]

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Input: s = ")("
Output: [""]

openCount = 1
closeCount = 1
"("

if openCount < closeCount:
    remove the bracket
"""

import collections

def removeInvalidParanthesisBFS(s: str) -> str:
    def isValid(string):
        balance = 0
        for ch in string:
            if ch == '(':
                balance += 1
            elif ch == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    if not s or isValid(s): return [s]

    ans = []
    q = [s, '#']
    seen = set()
    seen.add(s)

    balanced = False
    while q:
        string = q.pop(0)
        if string == '#':
            if balanced:
                break
            q.append(string)
            continue
        
        if isValid(string):
            ans.append(string)
            balanced = True
        
        if balanced:
            continue
        
        for i, ch in enumerate(string):
            if ch not in '()': continue
            newStr = string[:i]+string[i+1:]
            if newStr in seen: continue
            seen.add(newStr)
            q.append(newStr)
    return ans

def removeInvalidParanthesisDFS(s: str) -> str:
    res = collections.defaultdict(set)
    def dfs(index, string, openCount=0, closeCount=0):
        if index >= len(s):
            if openCount == closeCount:
                res[len(string)].add(string)
            return
        if s[index] not in '()': 
            dfs(index+1, string+s[index], openCount, closeCount)
        else:
            if s[index] == '(':
                dfs(index+1, string+s[index], openCount+1, closeCount)
            elif closeCount+1 <= openCount:
                dfs(index+1, string+s[index], openCount, closeCount+1)
            dfs(index+1, string, openCount, closeCount)
    
    dfs(0, '', 0, 0)
    keys = sorted(res.keys(), key=lambda k: k)
    return list(res[keys[-1]])

print(removeInvalidParanthesisDFS('()())()'))
print(removeInvalidParanthesisBFS('()())()'))

print(removeInvalidParanthesisDFS(''))
print(removeInvalidParanthesisBFS(''))

print(removeInvalidParanthesisDFS('(a)())()'))
print(removeInvalidParanthesisBFS('(a)())()'))

print(removeInvalidParanthesisDFS(')('))
print(removeInvalidParanthesisBFS(')('))


