'''
Write a function that returns the longest palindrome substring of a given string.
'''


def longest_palindrome(string):

    if len(string) < 2:
        return None

    def is_palindrome(string):
        l, r = 0, len(string) - 1

        while l < r:
            if string[l] != string[r]:
                return False
        return True

    longest_palindrome = ""
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if is_palindrome(string[i:j]):
                if len(string[i:j]) > len(longest_palindrome):
                    longest_palindrome = string[i:j]
                elif len(string[i:j]) == len(longest_palindrome):
                    if string[i:j] < longest_palindrome:
                        longest_palindrome = string[i:j]

    return longest_palindrome


# Test case 1
string = "racecarbobracecar"
assert longest_palindrome(string) == "racecar"

# Test case 2
string = "deifiedmadamdeified"
assert longest_palindrome(string) == "deified"

# Test case 3
string = "hannahandhermom"
assert longest_palindrome(string) == "hannah"

# Test case 4
string = "abacabbbba"
assert longest_palindrome(string) == "abbba"

# Test case 5
string = "abcdcba"
assert longest_palindrome(string) == "abcdcba"

# Test case 6
string = "abcdefg"
assert longest_palindrome(string) == None

# Test case 7
string = "aa"
assert longest_palindrome(string) == "aa"

# Test case 8
string = "abcbadefedcga"
assert longest_palindrome(string) == "abcba"
