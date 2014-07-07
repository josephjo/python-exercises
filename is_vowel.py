""" Return true if character is a vowel """
def is_vowel(char):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    if char in vowels:
        return True
    else:
        return False


print is_vowel("I") # True
print is_vowel("a") # True
print is_vowel("z") # False
print is_vowel("Q") # False
print is_vowel(3) # False
