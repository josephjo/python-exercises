import random
import string


""" Python function to generate text via random chars and ints """
def rand_gen(length):
    rand = []

    for i in range(length * 2):
        rand += str(random.randint(0, 9))

    for j in range(length * 2):
        rand += random.choice(string.letters)

    for k in range(length):
        rand += random.choice(string.punctuation)

    rand_string = random.shuffle(rand)

    rand_string = "".join(rand[:length])
    return rand_string


print rand_gen(10)
