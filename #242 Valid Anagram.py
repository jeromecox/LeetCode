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
