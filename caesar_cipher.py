import string


""" Implement a ROT-13 Caesar cipher encoder/decoder """
def caesar_cipher(text):
    decoded_text = ""
    key = {"a":"n", "b":"o", "c":"p", "d":"q", "e":"r", "f":"s", "g":"t", "h":"u",
           "i":"v", "j":"w", "k":"x", "l":"y", "m":"z", "n":"a", "o":"b", "p":"c",
           "q":"d", "r":"e", "s":"f", "t":"g", "u":"h", "v":"i", "w":"j", "x":"k",
           "y":"l", "z":"m", "A":"N", "B":"O", "C":"P", "D":"Q", "E":"R", "F":"S",
           "G":"T", "H":"U", "I":"V", "J":"W", "K":"X", "L":"Y", "M":"Z", "N":"A",
           "O":"B", "P":"C", "Q":"D", "R":"E", "S":"F", "T":"G", "U":"H", "V":"I",
           "W":"J", "X":"K", "Y":"L", "Z":"M"}

    for letter in text:
        if letter in string.letters:
            decoded_text += key[letter]
        else:
            decoded_text += letter

    return decoded_text


print caesar_cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")
print caesar_cipher("Grandpa?")
