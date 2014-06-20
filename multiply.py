""" For a list of integers, print the product """
def multiply(numbers):
    total = 1
    for num in numbers:
        total = total * num

    print "The total is %s." % total


multiply([10, 2, 1])
