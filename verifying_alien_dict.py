"""
Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""

from typing import List

"""
words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"

hlabcdefgijkmnopqrstuvwxyz
012345678.....
"""
def isSorted(words: List[str], order: str) -> bool:
    arr = [-1]*len(order)
    for i, ch in enumerate(order):
        arr[ord(ch)-ord('a')] = i
    
    for i in range(len(words)-1):
        # word, world
        word1, word2 = words[i], words[i+1]
        isPrefix = True
        for j in range(min(len(word1), len(word2))):
            ord1 = ord(word1[j])-ord('a')
            ord2 = ord(word2[j])-ord('a')
            if arr[ord1] == arr[ord2]: continue
            elif arr[ord1] > arr[ord2]: 
                isPrefix = False
                return False
            else: 
                isPrefix = False
                break
            
        if isPrefix and len(word1) > len(word2): return False
    
    return True

testCases = [
    [["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True],
    [["word","world","row"], "worldabcefghijkmnpqstuvxyz", False],
    [["apple","app"], "abcdefghijklmnopqrstuvwxyz", False],
]

for t in testCases:
    actual = isSorted(t[0], t[1])
    print('Expected: {}, Actual: {}'.format(t[2], actual))