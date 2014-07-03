""" Given a string, if length is at least 3
    add "ing" to its end. If it already ends
    in "ing" add "ly" instead.
"""
def verbing(word):
    if (len(word) > 2):
        if word[-3:] == "ing":
            return word + "ly"
        else:
            return word + "ing"
    else:
        return word


print verbing("Ow") # Ow
print verbing("Eating") # Eatingly
print verbing("Slow") # Slowing
print verbing("swimming")
