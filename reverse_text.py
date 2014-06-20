""" Reverses a given string """
def reverse_text(text):
    reversed_array = []
    y = 1

    for x in text:
        while y < len(text) + 1:
            reversed_array.append(text[-y])
            y = y + 1

    reverse = "".join(reversed_array)
    print reverse


reverse_text("Hello world!")
