import random
import string


""" Python function to generate text via random chars and ints """
class RandomGenerator(object):
    rand = []

    def __init__(self):
        super(RandomGenerator, self).__init__()

    """ Generate random chars, scramble them, and limit by given length """
    def rand_gen(self, length):
        self.gen_numbers(length)
        self.gen_letters(length)
        self.gen_symbols(length)

        rand_string = random.shuffle(self.rand)
        rand_string = "".join(self.rand[:length])
        return rand_string

    """ Generate random numbers """
    def gen_numbers(self, length):
        for i in range(length * 2):
           self.rand += str(random.randint(0, 9))

    """ Generate random letters """
    def gen_letters(self, length):
        for j in range(length * 2):
            self.rand += random.choice(string.letters)

    """ Generate random symbols """
    def gen_symbols(self, length):
        for k in range(length):
            self.rand += random.choice(string.punctuation)


std = RandomGenerator()
print std.rand_gen(10)
print std.rand_gen(5)
