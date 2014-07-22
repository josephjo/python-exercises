""" Given a list of words and a number, return list of words that are longer
    than the number """
def filter_long_words(list, length):
    filtered_words = ""

    for word in list:
        if len(word) > length:
            filtered_words += word + "\n"

    return filtered_words


print filter_long_words(["cat", "dog", "giraffe", "hippo"], 4)
