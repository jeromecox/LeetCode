'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


def isValid(string):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    hashmap = {")": "(", "]": "[", "}": "{"}

    for char in string:
        if char not in hashmap:
            stack.append(char)
            continue
        if not stack or stack[-1] != hashmap[char]:
            return False
        stack.pop()

    return not stack


# Test case 1
string = '()'
if isValid(string):
    print('Test 1 passes')

# Test case 2
string2 = '()[]{}'
if isValid(string2):
    print('Test 2 passes')

# Test case 3
string3 = '(]'
if not isValid(string3):
    print('Test 3 passes')
