"""
Custom Sort String

You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Input: order = "cbae", s = "abaacdbcbd"
Output: "ccbbbaaadd"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

O(26)
{
    d: 1
}
"""

def customSort(order: str, s: str) -> str:
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    
    ans = ''
    for ch in order:
        if ch in freq:
            ans += ch*freq[ch]
            freq[ch] = 0
    
    for ch in freq:
        ans += ch*freq[ch]
    return ans

print(customSort('cba', 'abaacdbcbd'))