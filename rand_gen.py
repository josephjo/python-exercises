import random
import string


""" Python function to generate text via random chars and ints """
def rand_gen(num):
    rand = []

    for i in range(num):
        rand += random.choice(string.letters)

    rand_string = random.shuffle(rand)
    rand_string = "".join(rand)
    return rand_string


print rand_gen(4)
