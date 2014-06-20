""" Prints a string with a phrase censored """
def censor(text, word):
    if word in text:
        censor = len(word) * "*"
        print text.replace(word, censor)


censor("Taco Bell Warns Employees Against Directly Exposing Skin To Food.", "Taco Bell")
