'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

s1, t1 = 'anagram', 'nagaram'
s2, t2 = 'rat', 'car'


# SOLUTION 1
def is_anagram(s, t):
    return print(sorted(s) == sorted(t))


is_anagram(s1, t1)
is_anagram(s2, t2)


# SOLUTION 2
def is_anagram1(s, t):
    if len(s) != len(t):
        return print(False)

    return print(sorted(s) == sorted(t))


is_anagram1(s1, t1)
is_anagram1(s2, t2)


# SOLUTION 3
def is_anagram2(s, t):
    if len(s) != len(t):
        return print(False)

    num_S, num_T = {}, {}

    for i in range(len(s)):
        num_S[s[i]] = 1 + num_S.get(s[i], 0)
        num_T[t[i]] = 1 + num_T.get(t[i], 0)

    for key in num_S:
        if num_S[key] != num_T.get(key, 0):
            return print(False)

    return print(True)


is_anagram2(s1, t1)
is_anagram2(s2, t2)


# SOLUTION 4
def is_anagram3(s, t):
    if len(s) != len(t):
        return print(False)

    num_S, num_T = {}, {}

    for i in range(len(s)):
        num_S[s[i]] = 1 + num_S.get(s[i], 0)
        num_T[t[i]] = 1 + num_T.get(t[i], 0)
    return print(num_S == num_T)


is_anagram3(s1, t1)
is_anagram3(s2, t2)
