""" Prints the number of times a given number is in a list """
def count(sequence, item):
    count = 0

    for i in sequence:
        if i == item:
            count = count + 1

    print "List:", sequence
    print "%s is in the list %s times." % (item, count)


count([9, 1, 81, 1, 0, 2, 1, 90, 0, 1], 1)
