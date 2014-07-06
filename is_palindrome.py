""" Function that returns True if a word is a palindrome """
def is_palindrome(word):
    return word == word[::-1]

print is_palindrome("beautiful") # False
print is_palindrome("radar") # True
