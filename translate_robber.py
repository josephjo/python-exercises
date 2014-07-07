""" Translates a text into "The Robber Language", a Swedish language game.
    Double every consonant and place an occurrence of "o" in between.
"""
def translate_robber(text):
    not_consonant = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U", " "]
    new_text = ""

    for letter in text:
        if letter not in not_consonant:
            new_text += letter + "o" + letter.lower()
        else:
            new_text += letter
    print new_text


translate_robber("I am a robber!")
translate_robber("Lorem ipsum dolor sit amet")
