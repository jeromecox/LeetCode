'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
s = 'A man, a plan, a canal: Panama'
s1 = 'race a car'
s2 = ' '


# SOLUTION #1
def is_palindrome(s):
    s_alnum = ''.join(e for e in s if e.isalnum()).lower()

    if len(s_alnum) > 0:
        for i in range(int(len(s_alnum) / 2) + 1):
            if (s_alnum[i] != s_alnum[(-abs(i) - 1)]):
                return print(False)
    return print(True)


is_palindrome(s)
is_palindrome(s1)
is_palindrome(s2)
