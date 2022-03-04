"""
Integer to English Words
Convert a non-negative integer num to its English words representation.

Input: num = 123
Output: "One Hundred Twenty Three"

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

num = 2147483647
Output: "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
0 <= num <= 2^31-1
"""
        
def convert(num: int) -> str:
    if num == 0: return 'Zero'

    digits = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }

    teens = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
    }

    tenners = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety',
    }

    places = {
        10**9: 'Billion',
        10**6: 'Million',
        10**3: 'Thousand',
        100:   'Hundred',
    }

    def resolveNumToWord(num: int) -> str:
        place = 100
        x = num
        res = ''
        while x > 0:
            tmp = x % place
            x = x // place
            if place == 100:
                if x > 0:
                    phrase = digits[x] + ' ' + places[place]
                    res += ' ' + phrase if res else phrase

                if 9 < tmp < 20:
                    phrase = teens[tmp]
                    res += ' ' + phrase if res else phrase
                    break
            elif place == 10 and x > 1:
                phrase = tenners[x]
                res += ' ' + phrase if res else phrase
            elif place == 1 and x > 0:
                phrase = digits[x]
                res += ' ' + phrase if res else phrase

            x = tmp
            place = place // 10
        return res
    
    place = 10**9
    ans = ''
    x = num
    while x > 0:
        tmp = x % place
        x = x // place
        if x > 0:
            phrase = resolveNumToWord(x)
            if place > 1:
                phrase += ' ' + places[place]
            ans += ' ' + phrase if ans else phrase
        x = tmp
        place = place // 10**3
    
    return ans

testCases = [
    [2**31-1, 'Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven'],
    [0, 'Zero'],
    [123467, 'One Hundred Twenty Three Thousand Four Hundred Sixty Seven'],
    [567, 'Five Hundred Sixty Seven'],
    [99, 'Ninety Nine'],
    [199, 'One Hundred Ninenty Nine'],
    [119, 'One Hundred Nineteen'],
    [103, 'One Hundred Three'],
    [12345, 'Twelve Thousand Three Hundred Forty Five']
]

for t in testCases:
    actual = convert(t[0])
    print('Expected: {}, Actual: {}'.format(t[1], actual))