"""
Strobogrammatic number

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Input: num = "69"
Output: true

Input: num = "88"
Output: true

Input: num = "962"
Output: false


"""

def isStrobo(num: str) -> bool:
    m = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6',
    }

    i = 0
    j = len(num)-1
    while i <= j:
        if num[i] not in m: return False
        if m[num[i]] != num[j]: return False
        i += 1
        j -= 1
    return True

print(isStrobo('123'))
print(isStrobo('111'))
print(isStrobo('69'))
print(isStrobo('96'))
print(isStrobo('00'))
print(isStrobo('808'))
print(isStrobo('858'))