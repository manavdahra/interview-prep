"""
Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
"""

"""
i = 12
j = 6
num = '4'
offset = 4

substitution
sub4u4
"""
def isValidAbbr(word: str, abbr: str) -> bool:
    i, j = 0, 0

    num = ''
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            num += abbr[j]
            j += 1
            continue
        if not num:
            if word[i] != abbr[j]: return False
            i += 1
            j += 1
        else:
            if num[0] == '0': return False
            offset = int(num)
            num = ''
            i += offset
    
    if num:
        if num[0] == '0': return False
        offset = int(num)
        num = ''
        i += offset
    
    return i == len(word) and j == len(abbr)

print(isValidAbbr('substitution', 'sub4u4'))
print(isValidAbbr('internationalization', 'i12iz4n'))
print(isValidAbbr('substitution', 'su3i1u2on'))
print(isValidAbbr('substitution', '12'))

print(isValidAbbr('apple', 'a2e'))
print(isValidAbbr('substitution', 's010n'))