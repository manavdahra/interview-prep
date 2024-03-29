"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

nput: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

def isValid(s: str) -> bool:
    res = []
    for ch in s:
        if ch.isalnum():
            res.append(ch.lower())
    
    i, j = 0, len(res)-1
    while i < j:
        if res[i] != res[j]:
            return False
        i += 1
        j -= 1
    return True

print(isValid("A man, a plan, a canal: Panama"))
print(isValid("race a car"))
print(isValid(" "))