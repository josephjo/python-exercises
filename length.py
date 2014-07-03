""" Function that computes the length of a given argument """
def length(arg):
    count = 0

    for letter in arg:
        count += 1

    print "The length of '%s' is %s." % (arg, count)


length("Cat") # 3
length([3, 4, 2, 1, 12]) # 5
