'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

strs = ["eat","tea","tan","ate","nat","bat"]
strs1 = [""]
strs2 = ["a"]


# SOLUTION 1
def group_anagrams(strs):
    hash_map = {}

    for word in strs:
        count = [0] * 26

        for letter in word:
            count[ord(letter) - ord('a')] += 1
        count = tuple(count)
        hash_map[count] = [word] + hash_map.get(count, [])
    return print(hash_map.values())


group_anagrams(strs)
group_anagrams(strs1)
group_anagrams(strs2)
