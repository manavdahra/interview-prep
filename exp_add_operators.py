"""
Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

helper(index, curr, prev, exp, expStr):

    curr = curr*10 + num[index]
    if curr > 0:
        helper(index+1, curr, prev, exp, expStr)
    if not expStr:
        helper(index+1, 0, curr, exp+curr, str(curr))
    else:
        helper(index+1, 0, curr, exp+curr, expStr+'+'+str(curr))
        helper(index+1, 0, -curr, exp-curr, expStr+'-'+str(curr))
        helper(index+1, 0, curr, exp-prev + prev*curr, expStr+'*'+str(curr))

105
1*05
1+05

"""

def addOpers(num: str, target: int):

    ans = []

    def helper(index, curr, prev, exp, expStr):
        if index >= len(num):
            if exp == target and curr == 0:
                ans.append(expStr)
            return

        curr = curr*10 + int(num[index])
        if curr > 0:
            helper(index+1, curr, prev, exp, expStr)
        if not expStr:
            helper(index+1, 0, curr, exp+curr, str(curr))
        else:
            helper(index+1, 0, curr, exp+curr, expStr+'+'+str(curr))
            helper(index+1, 0, -curr, exp-curr, expStr+'-'+str(curr))
            helper(index+1, 0, curr*prev, exp-prev + prev*curr, expStr+'*'+str(curr))

    helper(0, 0, 0, 0, '')
    return ans

print(addOpers('123', 6))
print(addOpers('232', 8))
print(addOpers('3456237490', 9191))