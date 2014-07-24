""" Find the longest word in a list of words. """
def find_longest_word(list):
    max_word = ""
    max_length = 0

    for word in list:
        if len(word) > max_length:
            max_word = word

    print max_word, "is the longest word with %s letters." % len(word)


find_longest_word(["cat", "dog", "giraffe"])
