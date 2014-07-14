import random
import string


""" Python function to generate text via random chars and ints """
def rand_gen(num):
    rand = []

    for i in range(num):
        rand += str(random.randint(0, 9))

    for j in range(num):
        rand += random.choice(string.letters)

    for k in range(num / 2):
        rand += random.choice(string.punctuation)

    rand_string = random.shuffle(rand)
    rand_string = "".join(rand)
    return rand_string


print rand_gen(4)
