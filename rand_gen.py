import random
import string


class RandomGenerator(object):
    rand = []

    """ Python function to generate text via random chars and ints """
    def __init__(self):
        super(RandomGenerator, self).__init__()

    def rand_gen(self, length):
        grades = self.gen_numbers(length)
        self.gen_symbols(length)
        self.gen_symbols(length)

        rand_string = random.shuffle(self.rand)

        rand_string = "".join(self.rand[:length])
        return rand_string

    def gen_numbers(self, length):
        for i in range(length * 2):
           self.rand += str(random.randint(0, 9))

    def gen_letters(self, length):
        for j in range(length * 2):
            self.rand += random.choice(string.letters)

    def gen_symbols(self, length):
        for k in range(length):
            self.rand += random.choice(string.punctuation)


std = RandomGenerator()
print std.rand_gen(10)
print std.rand_gen(5)
