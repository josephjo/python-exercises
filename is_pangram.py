import string


"""
    Check to see if a sentence is a pangram (a sentence using every letter of
    the alphabet at least once).
"""
def is_pangram(s):
    alphabet = string.lowercase
    s = s.lower()

    for letter in s:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")

    if alphabet == "":
        print "Yes, this is an pangram!"
    else:
        print "No, this is not an pangram. \"%s\" was not used." % alphabet


is_pangram("Nymphs blitz quick vex dwarf jog") # True
is_pangram("Cwm fjord veg balk nth pyx quiz") # False
is_pangram("Dog") # False
is_pangram("Grumpy wizards make toxic brew for the evil queen and jack") # True
