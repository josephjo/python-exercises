""" Print a string without any vowels """
def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for letter in text:
        if letter in vowels:
            text = text.replace(letter, "")
    print text


remove_vowels("The quick brown fox jumps over the lazy dog.")
