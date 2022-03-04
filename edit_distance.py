"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""

def dist(word1: str, word2: str) -> int:
    """
    rosse
    ros

    """
    def helper(i, j, mem={}):
        if (i, j) in mem: return mem[i, j]
        if i >= len(word1) and j >= len(word2):
            return 0
        if j >= len(word2):
            mem[i, j] = 1+helper(i+1, j)
            return mem[i, j]
        if i >= len(word1):
            mem[i, j] = 1+helper(i, j+1)
            return mem[i, j]
        
        if word1[i] == word2[j]:
            mem[i, j] = helper(i+1, j+1)
            return mem[i, j]
        
        mem[i, j] = 1 + min(
            helper(i+1, j), # adding character
            helper(i, j+1), # removing character
            helper(i+1, j+1), # replacing character
        )
        return mem[i, j]
    return helper(0, 0)

testCases = [
    ['horse', 'ros', 3],
    ['intention', 'execution', 5]
]

for t in testCases:
    actual = dist(t[0], t[1])
    print('Expected: {}, Actual: {}'.format(t[2], actual))
